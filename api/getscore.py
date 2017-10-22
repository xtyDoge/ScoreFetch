import re
import json
import requests
from bs4 import BeautifulSoup

def getScoreInfo(session):
		#采用MAP和.contents来提取出来所有的子节点，不要最后一个，然后按照顺序放进字典 做成JSON
		def getChildContent(lsn):
			#lsn是一个迭代器
			tmpList = []
			lessonInfoList = []
			lessonGradeList = []
			lessonInfoDict = {'CourseSerial':'','CourseName':'','EngName':'','Credit':'','Attribute':''}
			lessonGradeDict = {}
			#遍历出来lsn
			for child in lsn.children:
				tmpList.append(child)
			#正则表达式去掉换行符制表符回车
			p = re.compile('\s+')
			for x in range(1,len(tmpList)-2):				
				tmpList[x] = re.sub(p,'',tmpList[x].string)
			#用tmplist（NavigableString）填充两个字典
			#只有一个键值对{课程号：分数}	
			# lessonGradeDict[tmpList[1]] = re.sub(p,'',tmpList[-2].find('p').string)
			#很乱 td好像不是浏览器显示的那样，中间有很多制表符
			#lessonInfoDict['CourseNo'] = tmpList[1]
			lessonInfoDict['CourseSerial'] = tmpList[3]
			lessonInfoDict['CourseName'] = tmpList[5]
			lessonInfoDict['EngName'] = tmpList[7]
			lessonInfoDict['Credit'] = tmpList[9]
			lessonInfoDict['Attribute'] = tmpList[-4]
			lessonInfoDict['CourseNo'] = tmpList[1]
			lessonInfoDict['Grade'] = re.sub(p,'',tmpList[-2].find('p').string)
			#{Info:{课程号：{其余信息}}}
			return lessonInfoDict
		_url = "http://jwxt.bupt.edu.cn/"
		req = session.get(_url + "gradeLnAllAction.do?type=ln&oper=qbinfo&lnxndm=2015-2016%D1%A7%C4%EA%B5%DA%B6%FE%D1%A7%C6%DA(%B4%BA)(%C8%FD%D1%A7%C6%DA)")
		destnation = BeautifulSoup(req.text,"lxml")
		lessons = destnation.find_all("tr",class_="odd")
		#所有Lesson的信息放到一个列表中
		Total = list(map(getChildContent,lessons))


		GradeJson = {"Status":"Success","Content":Total}
		# print(GradeJson)
		print("......Total %s Records of lessons......" % len(Total))
			
		return GradeJson
