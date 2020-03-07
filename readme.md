# 单词出现频率统计
## 测试背景
    Word_Counter类要求读取一个英文的文本文件，统计其中单词出现的频率
### 测试内容：
##### 若txt文件存在且格式正确：
    返回值为所有单词出现的频率
    例如 txt文件内容为“hello world hello Python hello git”
    返回值为“hello（3） world（1） Python（1） git（1）”
##### 若txt文件存在但文件格式不对;
    文件中中只有一个单词或所有单词中间无间隔：
    返回值为该字符串
    例如 txt文件内容为“helloworld”
    返回值为“helloworld（1）”
    文件为空：
    返回值为“null”
##### 若txt文件不存在：
    文件不存在则返回“error”
#### 数据结构的选择
    一个单词对应一个出现的频率，所以此处选择dict来统计，单词作为key，频率作为对应的值
