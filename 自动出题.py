import random #line:1:import random
import re #line:2:import re
EXAM =[]#line:3:EXAM = []
num =0 #line:4:num = 0
def find_question (OO0O000OO0O000OOO ):#line:6:def find_question(string):
	O000OO0OO000O00O0 =re .compile (r'.*是\(\)')#line:7:rule = re.compile(r'.*是\(\)')
	OOOOOOOOOO0000000 =O000OO0OO000O00O0 .search (OO0O000OO0O000OOO )#line:8:result = rule.search(string)
	return OOOOOOOOOO0000000 .group ()#line:9:return result.group()
def find_answer (O00OO00O0OOO0OOO0 ):#line:11:def find_answer(string):
	OOO00OOOOOO000000 =re .compile (r'是\(\).*$')#line:12:rule = re.compile(r'是\(\).*$')
	O00OO00OO0O00000O =OOO00OOOOOO000000 .search (O00OO00O0OOO0OOO0 )#line:13:result = rule.search(string)
	O00OO00OO0O00000O =re .sub ('是\(\)',' ',O00OO00OO0O00000O .group ())#line:14:result = re.sub('是\(\)',' ',result.group())
	O00OO00OO0O00000O =re .sub ('\t','$',O00OO00OO0O00000O )#line:15:result = re.sub('\t', '$', result)
	O00OO00OO0O00000O =re .sub ('\n','$',O00OO00OO0O00000O )#line:16:result = re.sub('\n', '$', result)
	O00OO00OO0O00000O =O00OO00OO0O00000O .replace ('$','',1 )#line:17:result = result.replace('$','',1)
	O00OO00OO0O00000O =O00OO00OO0O00000O .split ('$')#line:18:result = result.split('$')
	random .shuffle (O00OO00OO0O00000O )#line:19:random.shuffle(result)
	OOOOOOO00O0OOOOOO ='\n(A) '+O00OO00OO0O00000O [0 ]+'\t\t(B) '+O00OO00OO0O00000O [1 ]+'\n(C) '+O00OO00OO0O00000O [2 ]+'\t\t(D) '+O00OO00OO0O00000O [3 ]#line:20:ANSWER = '\n(A) '+result[0]+'\t\t(B) '+result[1]+'\n(C) '+result[2]+'\t\t(D) '+result[3]
	return OOOOOOO00O0OOOOOO #line:21:return ANSWER
for line in open ('选择题库.txt',encoding ='utf-8'):#line:24:for line in open('选择题库.txt',encoding='utf-8'):
	line =line .strip ()#line:25:line = line.strip()
	question =find_question (line )#line:26:question = find_question(line)
	answer =find_answer (line )#line:27:answer = find_answer(line)
	sum =question +answer #line:28:sum = question+answer
	EXAM .append (sum )#line:29:EXAM.append(sum)
random .shuffle (EXAM )#line:30:random.shuffle(EXAM)
file =open ('XXX选择题库.txt','x')#line:31:file = open('XXX选择题库.txt','x')
for i in EXAM :#line:32:for i in EXAM:
	num +=1 #line:33:num += 1
	i =str (num )+'、'+i +'\n'#line:34:i = str(num)+'、'+i+'\n'
	file .write (i )#line:35:file.write(i)
