import { defineUserConfig } from "vuepress";

import theme from "./theme.js";

export default defineUserConfig({
  base: "/ddstudy/",

  locales: {
    "/zh/": {
      lang: "zh-CN",
      title: "ddstudy",
      description: "vuepress-theme-hope 的文档演示",
    },
    "/": {
      lang: "en-US",
      title: "Docs Demo",
      description: "A docs demo for vuepress-theme-hope",
    },
  },

  theme,

  // Enable it with pwa
  // shouldPrefetch: false,
});
