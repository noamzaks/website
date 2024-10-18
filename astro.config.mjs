import sitemap from "@astrojs/sitemap";
import { defineConfig } from "astro/config";
import astroOGImage from "./extensions/astroOGImage";
import { rehypeHeadingIds } from "@astrojs/markdown-remark";
import rehypeAutolinkHeadings from "rehype-autolink-headings";

// https://astro.build/config
export default defineConfig({
    site: "https://noamzaks.com",
    integrations: [sitemap(), astroOGImage()],
    markdown: {
        rehypePlugins: [
            rehypeHeadingIds,
            [
                rehypeAutolinkHeadings,
                {
                    content: {
                        type: "element",
                        tagName: "i",
                        properties: {
                            className: ["fa-solid", "fa-link", "heading-link"],
                        },
                        children: [],
                    },
                },
            ],
        ],
    },
    prefetch: {
        defaultStrategy: "viewport",
    },
});
