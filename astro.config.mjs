import sitemap from "@astrojs/sitemap";
import { defineConfig } from "astro/config";
import astroOGImage from "./extensions/astroOGImage";

// https://astro.build/config
export default defineConfig({
    site: "https://noamzaks.com",
    integrations: [sitemap(), astroOGImage()],
});
