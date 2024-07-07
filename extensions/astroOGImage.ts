// Based on https://github.com/tomaskebrle/astro-og-image

import type { AstroIntegration } from "astro";
import * as fs from "fs";
import { fileURLToPath } from "node:url";
import { relative, resolve } from "path";
import puppeteer from "puppeteer";

export default function astroOGImage(): AstroIntegration {
    return {
        name: "astro-og-image",
        hooks: {
            "astro:build:done": async ({ dir, routes }) => {
                // Filters all the routes that need OG image
                let filteredRoutes = routes;

                // Creates a directory for the images if it doesn't exist already
                let directory = fileURLToPath(new URL(`./thumbnails`, dir));
                if (!fs.existsSync(directory)) {
                    fs.mkdirSync(directory, { recursive: true });
                }

                const browser = await puppeteer.launch({
                    args: ["--no-sandbox", "--disable-setuid-sandbox"],
                });

                const promises: Promise<void>[] = [];
                for (const route of filteredRoutes) {
                    // Gets the title
                    const pathname = relative(
                        "./dist",
                        route?.distURL?.pathname ?? ""
                    );
                    // Skip URLs that have not been built (draft: true, etc.)
                    if (!pathname) {
                        continue;
                    }
                    const data = fs.readFileSync(
                        route!.distURL!.pathname as any,
                        "utf-8"
                    ) as any;
                    let title = await data.match(
                        /<title[^>]*>([^<]+)<\/title>/
                    )[1];
                    let description = await data.match(
                        /<meta name="description" content="(.*?)">/
                    )[1];
                    let icon = await data.match(
                        /<meta name="thumbnail-icon" content="(.*?)">/
                    )[1];

                    // Get the html
                    const html = fs
                        .readFileSync("og-image.html", "utf-8")
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
                        if (!fs.existsSync(directoryPath)) {
                            fs.mkdirSync(directoryPath, { recursive: true });
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
