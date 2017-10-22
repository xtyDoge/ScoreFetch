
def getGPA(content):
	GPASMCT = 0
	GPACT = 0
	SMCT = 0
	CT = 0
	cnt = 0
	for items in content:
		if items['Grade'] != "免修":
			GPASMCT = SMCT + float(items['Credit']) * float(items['Grade'])
			GPACT = CT + float(items['Credit'])
			if items['Attribute'] != "任选":
				print (items)
				cnt = cnt + 1
				SMCT = SMCT + float(items['Credit']) * float(items['Grade'])
				CT = CT + float(items['Credit'])
	Average = SMCT / CT
	GPA = (GPASMCT / GPACT) / 25
	resultDict = {"Average":Average,"GPA":GPA}
	# print(resultDict)
	return resultDict