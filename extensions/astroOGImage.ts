// Based on https://github.com/tomaskebrle/astro-og-image

import type { AstroIntegration } from "astro";
import { readdirSync, existsSync, mkdirSync, readFileSync } from "fs";
import { fileURLToPath } from "url";
import { join } from "path";
import { relative, resolve } from "path";
import puppeteer from "puppeteer";

export default function astroOGImage(): AstroIntegration {
    return {
        name: "astro-og-image",
        hooks: {
            "astro:build:done": async ({ dir }) => {
                let files = readdirSync(dir, { recursive: true })
                    .map((x) => join(fileURLToPath(dir), x.toString()))
                    .filter((x) => x.endsWith(".html"));

                // Creates a directory for the images if it doesn't exist already
                let directory = fileURLToPath(new URL(`./thumbnails`, dir));
                if (!existsSync(directory)) {
                    mkdirSync(directory, { recursive: true });
                }

                const browser = await puppeteer.launch({
                    args: ["--no-sandbox", "--disable-setuid-sandbox"],
                });

                const promises: Promise<void>[] = [];
                for (const f of files) {
                    // Gets the title
                    const pathname = relative("./dist", f ?? "");

                    const data = readFileSync(f, "utf-8");
                    let title = ((await data.match(
                        /<title[^>]*>([^<]+)<\/title>/
                    )) ?? [])[1];
                    let description = ((await data.match(
                        /<meta name="description" content="(.*?)">/
                    )) ?? [])[1];
                    let icon = ((await data.match(
                        /<meta name="thumbnail-icon" content="(.*?)">/
                    )) ?? [])[1];

                    if (!title || !description || !icon) {
                        continue;
                    }

                    // Get the html
                    const html = readFileSync("og-image.html", "utf-8")
                        .toString()
                        .replace("@curdir", resolve("."))
                        .replace("@title", title.split(" | ")[0])
                        .replace("@description", description)
                        .replace("@icon", icon);

                    const promise = browser.newPage().then(async (page) => {
                        await page.setContent(html);
                        await page.waitForNetworkIdle();
                        await page.setViewport({
                            width: 1200,
                            height: 630,
                        });

                        const split = pathname.split("/");
                        const filename = split[split.length - 1];
                        const directoryPath = relative(
                            ".",
                            fileURLToPath(
                                new URL(
                                    `./thumbnails/${split
                                        .slice(0, split.length - 1)
                                        .join("/")}${
                                        filename === "index.html"
                                            ? ""
                                            : "/" + filename.split(".")[0]
                                    }`,
                                    dir
                                )
                            )
                        );
                        if (!existsSync(directoryPath)) {
                            mkdirSync(directoryPath, {
                                recursive: true,
                            });
                        }

                        await page.screenshot({
                            path: `${directoryPath}/thumbnail.png`,
                            encoding: "binary",
                        });
                        await page.close();
                    });
                    promises.push(promise);
                }
                await Promise.all(promises);
                await browser.close();
            },
        },
    };
}
