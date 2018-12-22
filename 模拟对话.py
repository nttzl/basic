# -*- coding: utf-8 -*-
import time

tup1 = (1,2,3,4)
tup2 = ("你好！","你几岁了？","今天天气怎么样？","再见")
tup3 = ("你也好","10岁","阴天","再见")
l1 = list(zip(tup1,tup2))

print("你想说什么？：")

for i in range(4):
    print(l1[i])          #打印所有的问题
x = int(input())
while x != 4:
    print(tup2[x-1])
    time.sleep(1)         # 模拟思考的时间
    print(tup3[x-1])
    x = int(input())
else:                     # 当你说再见时，电脑回答再见，并不再继续对话
    print(tup2[3])
    time.sleep(1)
    print(tup3[3])
