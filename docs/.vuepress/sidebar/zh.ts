import { sidebar } from "vuepress-theme-hope";

export const zhSidebar = sidebar({
  "/zh/reading/zootopia/":"structure",
  "/zh/reading/哲学100问/":"structure",

  "/zh/ai/":"structure",

  "/zh/work/soft/":"structure",
  "/zh/work/database/":"structure",
  "/zh/work/bigdata/":"structure",
  "/zh/work/bigdata/apache/":"structure",

  "/zh/work/language/":"structure",
  
  "/zh/focus/高项/":[
    {
      text: "高项",
      children: ["考点", "计算", "论文/","论文_ly/"],
    },
  ],



  // "/zh/": [
  //   // "",
  //   // "portfolio",
  //   {
  //     text: "阅读",
  //     icon: "laptop-code",
  //     prefix: "reading/",
  //     link: "reading/",
  //     children: "structure",
  //   },
    
  //   {
  //     text: "案例",
  //     icon: "laptop-code",
  //     prefix: "demo/",
  //     link: "demo/",
  //     children: "structure",
  //   },
  //   {
  //     text: "文档",
  //     icon: "book",
  //     prefix: "guide/",
  //     children: "structure",
  //   },
  //   {
  //     text: "幻灯片",
  //     icon: "person-chalkboard",
  //     link: "https://ecosystem.vuejs.press/zh/plugins/markdown/revealjs/demo.html",
  //   },
  // ],
});
