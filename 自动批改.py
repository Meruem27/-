import re #line:1:import re
dic ={}#line:2:dic = {}
EXAM =[]#line:3:EXAM = []
right_number =0 #line:4:right_number = 0
def find_question (OO0000O0O0O00O0OO ):#line:6:def find_question(string):
	O00OO0O0OO0O00O0O =re .compile (r'、.*是\(')#line:7:rule = re.compile(r'、.*是\(')
	OO00000O0O00000OO =O00OO0O0OO0O00O0O .search (OO0000O0O0O00O0OO )#line:8:result = rule.search(string)
	OO00000O0O00000OO =re .sub ('、','',OO00000O0O00000OO .group (),1 )#line:9:result = re.sub('、', '', result.group(),1)
	OO00000O0O00000OO =re .sub ('\(','',OO00000O0O00000OO )#line:10:result = re.sub('\(', '', result)
	return OO00000O0O00000OO #line:11:return result
def find_answer (OOO000000OO00000O ):#line:13:def find_answer(string):
	O00O000OO00OO00O0 =re .compile (r'是(.*)。')#line:14:rule = re.compile(r'是(.*)。')
	OOOOOOO0O0OO00OO0 =O00O000OO00OO00O0 .search (OOO000000OO00000O )#line:15:result = rule.search(string)
	OOOOOOO0O0OO00OO0 =re .sub ('是\(','',OOOOOOO0O0OO00OO0 .group ())#line:16:result = re.sub('是\(', '', result.group())
	OOOOOOO0O0OO00OO0 =re .sub ('\)。','',OOOOOOO0O0OO00OO0 )#line:17:result = re.sub('\)。','',result)
	return OOOOOOO0O0OO00OO0 #line:18:return result
with open ('填空题答案.txt','r',encoding ='utf-8')as file1 :#line:21:with open('填空题答案.txt','r',encoding='utf-8') as file1:
	next (file1 )#line:22:next(file1)
	for line in file1 .readlines ():#line:23:for line in file1.readlines():
		line =line .strip ()#line:24:line = line.strip()
		line =line .replace ('()。','')#line:25:line = line.replace('()。','')
		line =line .split ('\t')#line:26:line = line.split('\t')
		dic [line [0 ]]=line [1 ]#line:27:dic[line[0]]=line[1]
file1 .close ()#line:28:file1.close()
file2 =open ("某同学考试卷.txt",'r+',encoding ='utf-8')#line:30:file2 = open("某同学考试卷.txt",'r+',encoding='utf-8')
for line in file2 .readlines ():#line:31:for line in file2.readlines():
	question =find_question (line )#line:32:question = find_question(line)
	answer =find_answer (line )#line:33:answer = find_answer(line)
	line =line .strip ('\n')#line:34:line = line.strip('\n')
	if (dic [question ]==answer ):#line:35:if(dic[question]==answer):
		EXAM .append (line +"该题答案是{}，考生答案是{}，答对了，增加4分。".format (dic [question ],answer )+'\n')#line:36:EXAM.append(line+"该题答案是{}，考生答案是{}，答对了，增加4分。".format(dic[question],answer)+'\n')
		right_number +=1 #line:37:right_number+=1
	else :#line:38:else:
		EXAM .append (line +"该题答案是{}，考生答案是{}，答错了， 不得分。".format (dic [question ],answer )+'\n')#line:39:EXAM.append(line+"该题答案是{}，考生答案是{}，答错了， 不得分。".format(dic[question],answer)+'\n')
file3 =open ("某同学考试卷.txt",'w+',encoding ='utf-8')#line:40:file3 = open("某同学考试卷.txt",'w+',encoding='utf-8')
for line in EXAM :#line:41:for line in EXAM:
	file3 .writelines (line )#line:42:file3.writelines(line)
file3 .writelines ("最终成绩：该考生答对了{}道题，最终成绩是{}分。".format (right_number ,right_number *4 )+'\n')#line:43:file3.writelines("最终成绩：该考生答对了{}道题，最终成绩是{}分。".format(right_number,right_number*4)+'\n')
file3 .writelines ("判卷人： Runhao Lin")#line:44:file3.writelines("判卷人： Runhao Lin")
