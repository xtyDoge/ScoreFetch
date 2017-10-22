# ScoreFetch
一个简单的北邮教务系统爬虫


### 简介
---
- 模拟登陆教务系统，自动识别验证码
- 爬取得到课程得分信息，计算GPA等

### 快速开始
---
#### 1. 准备
安装`requests`,`bs4`,`PIL`，`pytesseract`库，安装`tesseract-ocr`
#### 2. 开始
`./app.py`是入口，将`LoginSession`实例的用户名和密码设置为自己的学号和教务密码即可。
