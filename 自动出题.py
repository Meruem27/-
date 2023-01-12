import random
import re
EXAM = []
num = 0

def find_question(string):
	rule = re.compile(r'.*是\(\)')
	result = rule.search(string)
	return result.group()

def find_answer(string):
	rule = re.compile(r'是\(\).*$')
	result = rule.search(string)
	result = re.sub('是\(\)',' ',result.group())
	result = re.sub('\t', '$', result)
	result = re.sub('\n', '$', result)
	result = result.replace('$','',1)
	result = result.split('$')
	random.shuffle(result)
	ANSWER = '\n(A) '+result[0]+'\t\t(B) '+result[1]+'\n(C) '+result[2]+'\t\t(D) '+result[3]
	return ANSWER

#以下为万金油语句
for line in open('选择题库.txt',encoding='utf-8'):
	line = line.strip()
	question = find_question(line)
	answer = find_answer(line)
	sum = question+answer
	EXAM.append(sum)
random.shuffle(EXAM)
file = open('XXX选择题库.txt','x')
for i in EXAM:
	num += 1
	i = str(num)+'、'+i+'\n'
	file.write(i)
