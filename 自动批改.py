import re
dic = {}
EXAM = []
right_number = 0

def find_question(string):
	rule = re.compile(r'、.*是\(')
	result = rule.search(string)
	result = re.sub('、', '', result.group(),1)
	result = re.sub('\(', '', result)
	return result

def find_answer(string):
	rule = re.compile(r'是(.*)。')
	result = rule.search(string)
	result = re.sub('是\(', '', result.group())
	result = re.sub('\)。','',result)
	return result

#以下为万金油语句
with open('填空题答案.txt','r',encoding='utf-8') as file1:
	next(file1)
	for line in file1.readlines():
		line = line.strip()
		line = line.replace('()。','')
		line = line.split('\t')
		dic[line[0]]=line[1]
file1.close()

file2 = open("某同学考试卷.txt",'r+',encoding='utf-8')
for line in file2.readlines():
	question = find_question(line)
	answer = find_answer(line)
	line = line.strip('\n')
	if(dic[question]==answer):
		EXAM.append(line+"该题答案是{}，考生答案是{}，答对了，增加4分。".format(dic[question],answer)+'\n')
		right_number+=1
	else:
		EXAM.append(line+"该题答案是{}，考生答案是{}，答错了， 不得分。".format(dic[question],answer)+'\n')
file3 = open("某同学考试卷.txt",'w+',encoding='utf-8')
for line in EXAM:
	file3.writelines(line)
file3.writelines("最终成绩：该考生答对了{}道题，最终成绩是{}分。".format(right_number,right_number*4)+'\n')
file3.writelines("判卷人： Runhao Lin")
