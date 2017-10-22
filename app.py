# app.py
# 程序入口

from tools.login import LoginSession
from api.getscore import getScoreInfo
from api.getgpa import getGPA

#创建一个登陆Session
session = LoginSession(username='yourname',password='yourpassword')

#获取分数信息
scoreinfo = getScoreInfo(session.Session())
print(scoreinfo)

#获取gpa信息
print(getGPA(scoreinfo['Content']))