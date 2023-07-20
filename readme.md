# PyUtils

尝试做一个通过 `Python` 实现的小工具集合，以满足我平时对各类文件的处理需求（而不需要去在线网站折腾）。

目前已有的功能如下：

```
📦pyUtils
 ┣ 📂pdf
 ┃ ┣ 📜merge - 合并多个pdf文件
 ┃ ┗ 📜split - 根据页码拆分pdf文件（至一个文件中）
```

请前往对应文件类型的目录下，查看对应的 `readme.md` 文档以了解每个功能的使用方式。

---

各个子目录的`requirements.txt`文件生成于`pipreqs`：

```shell
pipreqs ./ --encoding=utf-8
```
