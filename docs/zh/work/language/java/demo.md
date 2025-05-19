---
title: 案例
---


# 构建树

```
 public static void main(String[] args) {
        String[] data = {
                "1,0",
                "1_1,1",
                "1_2,1",
                "2,0",
                "1_1_1,1_1",
                "1_1_2,1_1",
                "1_1_2_1,1_1_2"
        };

        List<String> dataWithLevel = addLevelToData(data);

        for (String line : dataWithLevel) {
            System.out.println(line);
        }
    }

    private static List<String> addLevelToData(String[] data) {
        Map<String, Integer> levels = new HashMap<>();
        Map<String, String> allData = new HashMap<>();
        List<String> dataWithLevel = new ArrayList<>();

        int maxLevel = 0;


        // 获取所有元素和最大层级
        for (String line : data) {
            String[] parts = line.split(",");
            String currentElement = parts[0];
            String parentElement = parts[1];

            int parentLevel = levels.getOrDefault(parentElement, 0);
            int currentLevel = parentLevel + 1;
            levels.put(currentElement, currentLevel);
            maxLevel = currentLevel > maxLevel ? currentLevel: maxLevel;

            allData.put(currentElement,parentElement);
        }

        for (String line : data) {
            String[] parts = line.split(",");
            String currentElement = parts[0];
            String parentElement = parts[1];

            int parentLevel = levels.getOrDefault(parentElement, 0);
            int currentLevel = parentLevel + 1;

            currentElement = parentElement;
            ArrayList parentList = new ArrayList<String>();
            for(int i =0; i< currentLevel - 1; i++){
                String p1 = allData.getOrDefault(currentElement, "0");
                parentList.add(p1);
                currentElement = p1;
            }
            parentList = parentList.size() == 0 ? new ArrayList<>(Collections.singletonList("0")): parentList;
            Collections.reverse(parentList);
            String p = String.join(",", parentList);


            dataWithLevel.add(line + "," + currentLevel + "," + p);

        }


        String message = String.format("最大层级数：%s ", maxLevel);
        System.out.println(message);

        return dataWithLevel;
    }

```