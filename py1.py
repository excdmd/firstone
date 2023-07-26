# this is demo for test
# a 被赋值 6（把6放入a这个容器中）
#a = 2
a=60
# b 被复制5
b=5
#c被赋值a+b
c=a+b
#o不能为除数
#d=c/0
#输出c
print(c)

#如果c值大于40，输出("温度超过40度，报警。c的值为：" + str(c) )，否则·输出("温度小于或等于40度，正常。c的值为：" + str(c) )
if (c>40): 
    print("温度超过40度，报警。c的值为：" + str(c) )
    print("用tab对齐表示一段语句。")
    print("我是大于40哦")
   
else:
    print("温度小于或等于40度，正常。c的值为：" + str(c) )
    print("else 语句段")
    print('end')  