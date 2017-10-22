#login.py

#接受 账号/密码 来获得一个登录Session实例

import requests
from tools.validcode import validcode
from bs4 import BeautifulSoup

class LoginSession(object):
	"""登陆会话"""

	#利用requests库	
	def __init__(self, username ,password):
		self._session = requests.Session()
		self._url = "http://jwxt.bupt.edu.cn/"
		self._username = username
		self._password = password
		self._validcode = ""
		self._status = ''
	#向目标url发送get请求，拉取验证码，返回处理好的字符串验证码
	def getValidCode(self):
		self._session.get(self._url)
		req = self._session.get(self._url+"validateCodeAction.do?random=")
		return validcode(req.content)
	
	#配合识别的验证码拿到本次有效登陆的Session，返回
	def getSession(self):
		payload = {"type":"sso","zjh":self._username,"mm":self._password,"v_yzm":self.getValidCode()}
		pst = self._session.post(self._url+"jwLoginAction.do",data = payload)
		destnation = BeautifulSoup(pst.text,"lxml")
		#正则表达式匹配 <title>URP 综合教务系统 - 登录</title>没进去 学分制综合教务就是进去了
		if destnation.title.string == "URP 综合教务系统 - 登录":
			if len(destnation.find_all("font")) != 0 and destnation.find_all("font")[0].string == "你输入的证件号不存在，请您重新输入！":
				#重新输入证件号提示
				print("您的证件号不正确，请您重新输入！")
				self._status = 'USRERR'
				return False
			if len(destnation.find_all("font")) != 0 and destnation.find_all("font")[0].string == "您的密码不正确，请您重新输入！":
				#重新输入密码提示
				print("您的密码不正确，请您重新输入！")
				self._status = 'PWDERR'
				return False
			self._session = None
			self._session = requests.Session()
			self.getSession()
		else:
			print(destnation.title.string + "ENTERED!")#爬成功
			self._status = "SUCC"

	#返回拿到的session
	def Session(self):
		self.getSession()
		return self._session

