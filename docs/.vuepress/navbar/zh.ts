import { navbar } from "vuepress-theme-hope";

export const zhNavbar = navbar([
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
      "Words"
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
      "language/"
    ],
  },
  "/zh/life/",
  {
    text: "框架",
    prefix: "zh/frame/",
    children: [
      {
        text: "前端",
        prefix: "front/",
        children: [
          "vuepress2/",
          "vuepress-theme-hope/"
        ]
      },
      {
        text: "数据分析",
        prefix: "data/",
        children: [
          "pandas/"
        ]
      },
      {
        text: "ORM",
        prefix: "orm/",
        children: [
          "sqlalchemy/"
        ]
      },
      {
        text: "Web",
        prefix: "web/",
        children: [
          "SpringBoot"
        ]
      },
      {
        text: "gui",
        prefix: "gui/",
        children: [
          "tkinter",
          "tkinter-designer"
        ]
      },
      
    ]
  },
  {
    text: "人工智能",
    prefix: "zh/ai/",
    children: [
      {
        text: "框架",
        prefix: "frame/",
        children: [
          'Xinference'
          ,"Langchain-chatchat"
        ]
      },
      {
        text: "audio",
        prefix: "audio/",
        children: [
          'FunASR'
        ]
      },
      'prompt',
      'cursor/'
      
    ]
  },
  {
    text: "focus",
    prefix: "/zh/focus/",
    children: [
      'English/',
      {
        text: "高项",
        prefix: "高项/",
        children: [
          "案例", "计算", "论文/","论文_ly/"
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
