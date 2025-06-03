---
title: js
---

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