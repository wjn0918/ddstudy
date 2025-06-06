---
title: js
---

## 将逗号分隔的 name 属性转换为 value 数组

```
const input = [
  {
    "name": "a,b"
  },
  {
    "name": "a,b,c"
  }
];

// 1. 提取所有name属性并用逗号分割
// 2. 展平数组并去重
// 3. 转换为目标格式
const result = [...new Set(
  input
    .map(item => item.name.split(',')) // 分割成二维数组
    .flat()                           // 展平为一维数组
    .map(item => item.trim())         // 去除前后空格
)].map(value => ({ value }));         // 转换为目标格式

console.log(result);
```


## 某个原始重新排列，其他元素不变
```
const data = [
  { "x": "25.01", "y": 76408 },
  { "x": "25.10", "y": 152719 },
  { "x": "25.05", "y": 228439 },
  { "x": "25.07", "y": 152059 },
  { "x": "25.12", "y": 152578 },
  { "x": "25.02", "y": 76463 },
  { "x": "25.09", "y": 152779 },
  { "x": "25.04", "y": 76383 },
  { "x": "25.08", "y": 152897 },
  { "x": "25.03", "y": 76395 },
  { "x": "25.06", "y": 152880 },
  { "x": "25.11", "y": 152152 }
];
const newData = data
  .map((item, index) => ({
    x: `25.${String(index + 1).padStart(2, '0')}`,  // 重新生成 x 值
    y: item.y  // 保持 y 不变
  }));

```

## 数组过滤排序

```
const adcode = "11"; // 测试用，可以是 "", "11", 或 "1101"

const new_data = data
  .filter(item => {
    if (adcode.length === 0) return item.cj === 0;
    if (adcode.length === 2) return item.cj === 1;
    if (adcode.length === 4) return item.cj === 2;
    return false;
  })
  .sort((a, b) => b.mj - a.mj);

console.log(new_data);
```

## 数组计算
```
const data = [
  {
    "code": "",
    "name": "全国",
    "zt": "作业中",
    "sl": 36143
  },
  {
    "code": "",
    "name": "全国",
    "zt": "空闲中",
    "sl": 5122
  },
  {
    "code": "",
    "name": "全国",
    "zt": "故障",
    "sl": 87
  }
];

const total = data.reduce((sum, item) => sum + item.sl, 0);

console.log(total); // 输出: 41352
```


## 数组更改key

```
const data = [
  {
    "code": "00",
    "name": "全国",
    "mj": 25590.88
  }
];

const newData = data.map(({ mj, ...rest }) => ({
  ...rest,
  value: mj
}));

console.log(newData);
```


## 数组过滤

```
const data = [
  {id: 1, value: "22145"},
  {id: 2, value: "12345"},
  {id: 3, value: "22000"},
  {id: 4, value: "22567"},
  {id: 5, value: "11111"}
];

const filteredData = data.filter(item => item.value.startsWith("22"));
```

## 两个数组过滤

```
const namesToFilter = new Set(array2.map(item => item.name));
const filtered3 = array1.filter(item => namesToFilter.has(item.name));
```

## 两个数组关联
```
const array1 = [
  { id: 1, name: 'Apple', price: 1.2 },
  { id: 2, name: 'Banana', price: 0.5 },
  { id: 3, name: 'Orange', price: 0.8 }
];

const array2 = [
  { name: 'Apple', quantity: 10 },
  { name: 'Banana', quantity: 20 },
  { name: 'Orange', quantity: 15 }
];

// 按 name 关联两个数组
const mergedArray = array1.map(item1 => {
  const item2 = array2.find(item2 => item2.name === item1.name);
  return { ...item1, ...item2 };
});

console.log(mergedArray);
```


## 复制浏览器中变量
var a = 1
copy(a)

## 替换数组中对象的属性

```
{...obj, key=newValue}
```