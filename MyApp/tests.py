from django.test import TestCase

# Create your tests here.


# print([[""]*3 for i in range(4)])
# print([["" for i in range(3)] for j in range(4)])

# a = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 3]]
# print(a[0])
# a[0] = []
# top = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 3]]
# top2 = []
# for i in top:
#     new = []
#     for j in i:
#         new.append(str(j))
#     top2.append(new)
# print(top2)
# top = top2
# print(top)
# a = [[1,11],[1,100],[2,12],[11,22]]
# a.sort()
# print(a)
# a = 3
# if a == 3:
#     a = 2
# if a == 2:
#     print("ok")
# a = [[1,11],[1,100],[2,12],[11,22]]
# a[0][0] = 1
# print(a[0][0])

# a = "abbddddyyyyyppppp"
# flag = 1
# for i in range(len(a)-1):
#     if a[i] == a[i+1]:
#         flag += 1
#         if i == len(a)-2:
#             print([i-flag+2,i+1])
#     else:
#         if flag >= 3:
#             print([i + 1 - flag, i])
#         flag = 1

# a = [["a","b"],["c","c"]]
# b = []
# dic = {}
# dic[1] = 2
# dic[2] = 3
# dic[1] = 4
# print(dic)
# for i in range(len(a)):
#     b.append(a[i][0])
#     b.append(a[i][1])
# print(b)


# leetcode付费 返回nums的长度为k的最大子串（最大指从第一个元素开始比较，取最大，如果并列看第二个。以此类推下去）
# def largestSubarray(nums, k):


# print(largestSubarray([1, 4, 5, 2, 3], 4))

# import json
# a2 = {
#     "a":7,
#     "b":8
# }
# print(a2)
# b2 = json.dumps(a2)
# print(type(a2))
# print(type(b2))
# c2 = json.loads(b2)
# print("?"+c2)
# print(type(c2))

# a="123"
# b = a[:-1]
# print(b)

# import requests
# data = {
#         "key":"ab3dbb9ee014c253868403cd17d136ca",
#         "q":"掉牙"
#     }
# res = requests.request(url="http://v.juhe.cn/dream/query",method="post",data=data)
# print(res.text)
# print(type(res.text))
# print(res.content.decode())
# print(type(res.content.decode()))


# import requests
# data = {
#         "key":"ab3dbb9ee014c253868403cd17d136ca",
#         "q":"掉牙"
#     }
# res = requests.request(url="www.baidu.com/3e",method="get",headers={"Content-Type":"text/plain"},data="ff")
# print(res.text)

# a = '[["a","b"],["c","d"]]'
# for i in eval(a):
#     print(i[1])


# a = {
#     "a":1,
#     "b":"2"
# }
# a[3]=4
# print(a)
# def aa(a,k):
#     a[:] = a[len(a) - k:] + a[:len(a) - k]
#     return a
# a = [1,2,3,4,5,5,6,7]
# k = 4
# print(aa(a,k))


# a = [1,3,4,4,5]
# b = [3,5,9,4,4]
# c = set(a)&set(b)
# print(c)

# 统计一个数字在排序数组中出现的次数。
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2
# a = [1,2,3,0,0,0]
# a[:]=a[:3]+[9]+a[3:-1]
# print(a)
# a[:]=a[:4]+[10]+a[4:-1]
# print(a)



# a = {1,2}
# b = a
# b.add(3)
# print(a)
# print(b)

# import copy
# a = {
#     "a": 23
# }
# b = copy.deepcopy(a)
# b["a"] = 33
# print(a)
# print(b)

import json
# a = '{
#     "a": 23
# }'
# b = json.dumps(a)
# print(b)

# str = "'a',123,'',' ','./?*&^','中文'"
# a = str.split(",")
# print(type(eval(a[1])))

# import json
# a = 'ggg'
# json.loads(a)


# 第一道列表取第二大  不能用sort或者[-1]
# def get_second_big(a:list)->int:
#     for i in range(len(a)):
#         for j in range(i + 1, len(a) - 1):
#             if a[j] >= a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     a.pop()
#     return a.pop()
# a = [1,6,3,8,4,75,5]
# print(get_second_big(a))

# 第二道题是读取文件里面的所有时间格式
# def find_data_from_file(path:str):
#     import re
#     with open(path,encoding="utf-8") as f:
#         data = f.read()
#     res = re.findall("\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", data)
#     return res
# print(find_data_from_file("d://a.txt"))

# 第三道题是取文件夹下面的txt类型的文件
# def get_txt_file(file_path:str)->list:
#     import os
#     all_files = os.listdir(file_path)
#     res = []
#     for file in all_files:
#         if "txt"  in file:
#             res.append(file)
#     return res
# print(get_txt_file("d:/获取文件内所有txt"))

# import time
# newtime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
# print(newtime)
# begin = time.time()
# time.sleep(1)
# end = time.time()
# print("差距为:%.2f秒" % (end - begin))
# print(time.time())


# import datetime
# # 指定格式输出
# print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
# # 计算时间差
# begin = datetime.datetime(2020,1,1,16,0,0)
# end = datetime.datetime(2020,1,1,17,0,0)
# print((end - begin).days+1)
# print((end - begin).seconds)
# print(begin.year)
# print(datetime.datetime(2020,1,1,16,0,1).strftime("%Y-%m-%d %H-%M-%S"))

# import re
# with open("d://a.txt",encoding="utf-8") as f:
#     data = f.read()
# res = re.findall("\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", data)
# print(res)


# a = [0,0,0,1]
# while a[0] == 0:
#     del a[0]
# print(a)

# print(int("011",2))
# print(0b11)
# print(True if 0%5 == 0 else False)

# a = [{"1":22}, {"a":23}]
# b = json.dumps(a)
# print(b)
# print(type(b))
# c = json.loads(b)
# print(type(eval(b)[0]))

# a = [1,2,3]
# print(a[::-1])

# s = "anagram"
# t = "nagaram"
# a = sorted(s)
# b = sorted(t)
# print(a)
# print(b)
# print("ok" if a == b  else "gun")

# def isAnagram(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
#     import string
#     dic = {ss: 0 for ss in string.ascii_lowercase}
#     for i in s:
#         dic[i] += 1
#         print(dic)
#     for j in t:
#         dic[j] -= 1
#         print(dic)
#         if dic[j] < 0:
#             return False
#     return True
# print(isAnagram("ab", "a"))


for i in range(0,5,2):
    print(i)