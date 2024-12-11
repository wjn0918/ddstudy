import { navbar } from "vuepress-theme-hope";

export const zhNavbar = navbar([
  "/zh/",
  // "/zh/cookbook",
  // "/zh/portfolio",
  // "/zh/demo/",
  {
    text: "阅读",
    icon: "book",
    prefix: "/zh/reading/",
    children: [
      {
        text: "文学",
        children: [
          "zootopia/"
        ]
      },
      {
        text: "哲学",
        children: [
          "哲学100问/"
        ]
      },
    ]
  },
  {
    text: "工作",
    icon: "desktop",
    prefix: "/zh/work/",
    children: [
      "soft/",
      "os/",
      "database/",
      "bigdata/",
      "laguage/"
    ],
  },
  {
    text: "框架",
    prefix: "zh/frame/",
    children: [
      {
        text: "前端",
        prefix: "front/",
        children: [
          "vuepress-theme-hope/"
        ]
      }
    ]
  },
  // {
  //   text: "指南",
  //   icon: "lightbulb",
  //   prefix: "/zh/guide/",
  //   children: [
  //     {
  //       text: "Bar",
  //       icon: "lightbulb",
  //       prefix: "bar/",
  //       children: ["baz", { text: "...", icon: "ellipsis", link: "" }],
  //     },
  //     {
  //       text: "Foo",
  //       icon: "lightbulb",
  //       prefix: "foo/",
  //       children: ["ray", { text: "...", icon: "ellipsis", link: "" }],
  //     },
  //   ],
  // },
  // {
  //   text: "V2 文档",
  //   icon: "book",
  //   link: "https://theme-hope.vuejs.press/zh/",
  // },
]);
