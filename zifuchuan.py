#!/usr/bin/python3.4
# -*- coding=utf-8 -*-


# 通过字符串拼接的方式，打印出QYTANG'day 2014-9-28。不要忘记中间的空格。


# qytang = 'QYTANG'+'day'+'2014-9-28'
# print(qytang)

# ==========================================================================================

# 现在有个字符串word = " scallywag"，创建一个变量sub_word，通过切片的方式获得字符串"ally"，将字符串的内容赋予sub_word。

# word = " scallywag"
# sub_word = word[3:7]
# print(sub_word)

# ===========================================================================================

# 在单词的最后加上-，然后将单词的第一个字母拿出来放到单词的最后，然后在单词的最后加上y，例如，Python，就变成了ython-Py

# a = 'Python'
# b = a[1:]
# c = a[:1]
# d = a[1:2]
# e = str(b)+'-'+str(c)+str(d)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)


# ===========================================================================================
"""
deapartment1 = 'Security'
deapartment2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456


# line1 = 'Deapartment name:%-10s Manager:%-10s COURESS FEES:%-10.2f %-10s' % (deapartment1,depart1_m,COURSE_FEES_SEC,'THE END!')
# line2 = 'Deapartment name:%-10s Manager:%-10s COURESS FEES:%-10.2f %-10s' % (deapartment2,depart2_m,COURSE_FEES_Python,'THE END!')

test1 ='Deapartment name:{0:<10} Manager:{1:<10} COURESS FEES:{2:<10.2f}{3:>9}'
line1 = test1.format(str(deapartment1),str(depart1_m),float(COURSE_FEES_SEC),'THE END!')
test2 ='Deapartment name:{0:<10} Manager:{1:<10} COURESS FEES:{2:<10.2f}{3:>9}'
line2 = test2.format(str(deapartment2),str(depart2_m),float(COURSE_FEES_Python),'THE END!')

length = len(line1)
print('='*80)
print(line1)
print(line2)
print('='*80)

"""
# ===========================================================================================

import re
str1 = 'Port-channel1.189     192.168.189.254     YES   CONFIG    up'
interface = re.match('\s*(.*\.\d+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(YES|NO)\s+(CONFIG|DHCP)\s+(up|down)\s*',str1).groups()
line1 = '%-10s:%s' % ('接口',interface[0])
line2 = '%-10s:%s' % ('IP地址',interface[1])
line3 = '%-10s:%s' % ('状态',interface[4])
print('-'*50)
print(line1)
print(line2)
print(line3)









