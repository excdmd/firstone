# 连接到数据库
connection = MySQLdb.connect(host='localhost', user='root', passwd='password', db='database')

# 创建游标
cursor = connection.cursor()

# 执行查询
cursor.execute('SELECT * FROM tablename')

# 获取结果集
results = cursor.fetchall()

# 关闭游标
cursor.close()

# 关闭连接
connection.close()

# d = {'Alice': [50, 61, 66], 'Bob': [80, 61, 66], 'Candy': [88, 75, 90]}
# sc=d.values()
# print(len(sc))

# d = {'Alice': [50, 61, 66], 'Bob': [80, 61, 66], 'Candy': [88, 75, 90]}
# for key, value in d.items():
#     for score in value:
#         print(key, score)

# d = {'Alice': [50, 61, 66], 'Bob': [80, 61, 66], 'Candy': [88, 75, 90]}
# for key,value in d.items():
#     print(key,value)

# d = {
#     'Alice': 45,
#     'Bob': 60,
#     'Candy': 75,
#     'David': 86,
#     'Ellena': 49
# }
# print(d) # ==> {'Alice': 45, 'Bob': 60, 'Candy': 75, 'David': 86, 'Ellena': 49}
# alice_score= d.pop('Alice')
# print(alice_score) # ==> 45
# print(d) # ==> {'Bob': 60, 'Candy': 75, 'David': 86, 'Ellena': 49}
# print(d.keys())
# if 'Alice' in d.keys():
#     d.pop('Alice')
# print(d)    


# d = {
#     'Alice': 45,
#     'Bob': 60,
#     'Candy': 75,
#     'David': 86,
#     'Ellena': 49
# }
# print(d.get('Alice'))
# d['Alice']=45,60
# print(d)



# d = dict()
# d['Alice'] = []
# d['Bob'] = []
# d['Candy'] = []
# d['Alice'].append(50)
# d['Alice'].append(61)
# d['Alice'].append(66)
# d['Bob'].append(80)
# d['Bob'].append(61)
# d['Bob'].append(66)
# d['Candy'].append(88)
# d['Candy'].append(75)
# d['Candy'].append(90)

# d = {
#     'Alice': 45,
#     'Bob': 60,
#     'Candy': 75,
# }
# d['Alice']=[50,61,66]
# d['Bob']=[80,61,66]
# d['Candy']=[88,75,90]
# print(d)


# d = {
#     'Alice': 45,
#     'Bob': 60,
#     'Candy': 75,
#     'David': 86,
#     'Ellena': 49
# }

# d['Mimi'] = 72
# d['Dodo'] = 88
# print(d)

# names = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
# scores = [45, 60, 75, 86, 49]
# index = 0
# for name in names:
#     #score = scores[index]
#     print('name = {}, score = {}'.format(name,scores ))
#     #index = index + 1

# T = ((1+2),  ((1+2),), ('a'+'b'), (1, ), (1,2,3,4,5))
# print(T)
# print(id(T))
# print("%x" % id(T))

#a

# L = [[1,2,3], [5, 3, 2], [7,3,2]]
# for cube in L:
#     length = cube[0]
#     width = cube[1]
#     height = cube[2]
#     result = length * width * 2 + width * height * 2 + length * height * 2
#     print(result)

# a=[1, 2, 3]
# b=[5, 3, 2]
# c=[7, 3, 2]
# l= [a,b,c]
# s1=l[0][0]*l[0][1]*2+l[0][0]*l[0][2]*2+l[0][1]*l[0][2]*2
# print(s1)

# o=['Alice', 'Bob', 'Candy', 'David', 'Ellena']
# o[0]='ellena'
# o[1]='alice'
# o[2]='david'
# o[3]='candy'
# o[4]='bob'
# print(o)

# L = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
# L.pop(2)
# L.pop(3)
# print(L)

# w=['Alice', 'Bob', 'Candy', 'David', 'Ellena']
# w.append('zero')
# w.insert(-1,'gen')
# w.insert(-1,'phoebe')
# print(w)

# L = [95.5, 85, 59, 66, 72]
# print(L[0])
# print(L[1])
# print(L[4])

#1.排序输入list
#2.按顺序从高分到低分输出


# my_list = [1, 2, 3, 4, 5]

# print(my_list[3])

# num = 0
# L = ['Alice', 66, 'Bob', True, 'False', 100]
# for item in L:
#     num = num + 1
#     if num % 2 != 0:
#         continue
#     print(item)

# num=0

# L = ['Alice', 66, 'Bob', True, 'False', 100]
# for item in L:
#     num=num+1
#     if num%2==0:
#         print(item)
#     else:
#         num=num+0    


# s=['alice:','100','math:75','english:99']
# print(s)

# L = ['Alice','chinese',92,'math',75, 'english', 99]
# print(L)
# s1 = 'ABC'
# s2 = '123'
# s3 = '456'
# for y in s1:
#     for x in s2:
#         for z in s3:
#             print(x+y+z)
# print(x+y+z)

# a=1
# b=3
# c=a
# a=b
# b=c
# print(a,b)

# num=0
# a=0
# while True:
#     if num>1000:
#         break
#     num=num+1
#     if num%2==0:
#         a=a+num
#     else:
#         a=a+0
# print(a)
# s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# num = 1
# for ch in s:
#     if num < 3:
#         num = num + 1
#         continue # 当num < 10时，跳过后续循环代码，继续下一次循环else{
#     print(ch)
#     num = num + 1
# a=0
# b=0
# while a<1000:
#     # if a>6:
#     #     break
#     a=a+2
#     b=a+b
#     # if a>4:
#     #     break
# print(b)

# num=13
# if num%2==0:
#     print('{}是偶数'.format(num))
# elif num%2==1:
#     print('{}是ji数'.format(num))

# a=1
# b=0
# while b<10:
#     b=b+1
#     a=a*b
# print(a)


# L = [75, 92, 59, 68, 99]
#


# # age =18
# # if age<3:
# #     print('baby')
# # elif age<6:
# #     print('kid')
# # elif age<18:
# #     print('teenage')
# # elif age>=18:
# #     print('adult')

# # age=19
# # if age>=18:
# #     print('adult')
# # else:
# #     print('teenage')

# # age = 19
# # if age>18:
# #     print('your age={}'.format(age))
# #     print('adult')
# # s='AabCDEFGHHIJ'
# # res=s[1:]
# # print(res)

# #print('这是一句中英文混合的python字符串hello world!')
# # t='这是一句中英文混合的python字符串hello world'
# # print(t)

# #print('Bob said \n"I\'m OK\".')#'Bob said \"I\'m OK\".'
# #print('special striong:\',",\\,\\\\,\\n',)
# #get user name 
# # user=input('enter your name:')
# # print(user)
# # #get password
# # password=input('enter your password:')
# # print(password)

# # #get user name and password from database
# # sql='select age from people where name=user and pw=password'
# # # run sql get data
# # #下次深入学习 inert into people (name,password,age) values ('kite','ccs',33) 

# # # user=input('enter your name:')
# # # print(user)


# #'''print(r'''"To be,or not to be "that is the question.
# # Whether it's nobler in the mind to suffer.''')
# # age = 19
# # if age >= 18:
# #     print('give you a car',age)
# #     print('1give you a car',age)
# #     print('2give you a car',age)
# # else:
# #     print('gun!!',age)''')
