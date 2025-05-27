---
title: Component
---

[组件使用](https://theme-hope.vuejs.press/zh/guide/component/grammar.html)


```component VPCard
title: Mr.Hope
desc: Where there is light, there is hope
logo: https://mister-hope.com/logo.svg
link: https://mister-hope.com
background: rgba(253, 230, 138, 0.15)
```

```component VPCard
{
  "title": "Mr.Hope",
  "desc": "Where there is light, there is hope",
  "logo": "https://mister-hope.com/logo.svg",
  "link": "https://mister-hope.com",
  "background": "rgba(253, 230, 138, 0.15)"
}
```

## excel 组件展示
```

npm install @vue-office/excel vue-demi@0.14.6


<vue-office-excel
        :src="excel"
        style="height: 100vh;"
        @rendered="renderedHandler"
        @error="errorHandler"
    />

<script>
//引入VueOfficeExcel组件
import VueOfficeExcel from '@vue-office/excel'
//引入相关样式
import '@vue-office/excel/lib/index.css'

export default {
    components: {
        VueOfficeExcel
    },
    data() {
        return {
            excel: 'http://static.shanhuxueyuan.com/demo/excel.xlsx'//设置文档地址
        }
    },
    methods: {
        renderedHandler() {
            console.log("渲染完成")
        },
        errorHandler() {
            console.log("渲染失败")
        }
    }
}
</script>

```