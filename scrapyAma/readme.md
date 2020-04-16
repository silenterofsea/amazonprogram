# 主要思路
## scrapy + selenium 实现对amazone的登录
### 具体操作
- 首先要重写spider中start_request()方法， 用selenium来实现登录
- 其次在downldermiddleware中实现于selenium的对打开页面的读取
- 最后要结果返回出去

## 用scrapyrt对外暴露接口