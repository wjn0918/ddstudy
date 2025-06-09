import { navbar } from "vuepress-theme-hope";

export const zhNavbar = navbar([
  {
    text: "阅读篇",
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
      {
        text: "诗歌",
        children: [
          "poem/"
        ]
      },
      "Words"
    ]
  },
  {
    text: "工作篇",
    icon: "desktop",
    prefix: "/zh/work/",
    children: [
      "soft/",
      "os/",
      "database/",
      "bigdata/",
      "language/",
      "frame/",
    ],
  },
  {
    text: "聚焦篇",
    prefix: "/zh/focus/",
    children: [
      'stock/',
      'English/',
      'hellogithub',
      {
        text: "高项",
        prefix: "高项/",
        children: [
          "考点", "计算", "论文/", "论文_ly/"
        ]
      }
    ]
  },
  {
    text: "教学篇",
    prefix: "/zh/teaching/",
    children: [
      {
        text: "软件",
        prefix: "soft/",
        children: [
          "DataV/"
        ]
      }
    ]
  },
  "/zh/life/",
  "/zh/tools/",
  "/ME",
]);
