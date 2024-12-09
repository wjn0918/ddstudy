import { navbar } from "vuepress-theme-hope";

export const zhNavbar = navbar([
  "/zh/",
  "/zh/portfolio",
  "/zh/demo/",
  {
    text: "阅读",
    icon: "lightbulb",
    prefix: "/zh/reading/",
    children: [
      "zootopia/"
    ]
  },
  {
    text: "工作",
    icon: "lightbulb",
    prefix: "/zh/work/",
    children: [
      {
        text: "软件",
        icon: "lightbulb",
        prefix: "soft/",
        children: [
          "docker/", "datax/"
        ],
      },
      {
        text: "大数据",
        icon: "lightbulb",
        prefix: "bigdata/",
        children: [
          {
            text: "apache",
            icon: "lightbulb",
            link: "apache/"
          }
        ],
      },


      {
        text: "人工智能",
        icon: "lightbulb",
        prefix: "ai/",
        children: [
          {
            text: "apache",
            icon: "lightbulb",
            link: "apache/"
          }
        ],
      },
      {
        text: "数据库",
        icon: "lightbulb",
        prefix: "database/",
        children: [
          {
            text: "apache",
            icon: "lightbulb",
            link: "apache/"
          }
        ],
      },
      {
        text: "编程语言",
        icon: "lightbulb",
        prefix: "database/",
        children: [
          {
            text: "apache",
            icon: "lightbulb",
            link: "apache/"
          }
        ],
      },
      {
        text: "操作系统",
        icon: "lightbulb",
        prefix: "os/",
        children: [
          "linux/", "windows/"
        ],
      },
      

    ],
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
