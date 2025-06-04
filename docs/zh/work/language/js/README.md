---
title: js
---
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