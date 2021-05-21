# f=open('文件.txt','w')
# f.write('姓名：师玲珑\n年龄：18\n性别：男')
# f.close()

# f=open('文件.txt','r')

#read():
# content=f.read(11)
# print(content)
# print()
# content=f.read()
# print(content)

#readlines()
# list=f.readlines()
# print(list)
# for x in list:
#     print(x,end='')

#readline()
# content=f.readline()
# print("第一行内容有：%s"%content)
# content=f.readline()
# print("第二行内容有:%s"%content)

# f.close()

#修改文件.txt名字  os.rename
# import os
# os.rename('文件.txt','新文件.txt')

#删除文件  os.remove
# import os
# os.remove('新文件.txt')

#新建一个文件夹  os.mkdir
# import os
# os.mkdir('day12')

#删除一个文件夹  os.rmdir
# import os
# os.rmdir('day12')

#查看当前py的路径 os.getcwd
# import os
# print(os.getcwd())

#修改当前py路径  os.chdir
# import os
# os.chdir('../')
# print(os.getcwd())

#获取当前目录列表
# import os
# print(os.listdir('./'))  #查看的是当前目录列表
# print(os.listdir('../'))  #查看的是当前目录的上一级的目录列表


#文件备份
# oldname=input('请输入你要备份的文件名：')
# num=oldname.rfind('.')               #找到要备份文件的后缀名
# if num>0:                           #判断文件名是否存在
#     a=oldname[num:]                  #切出文件名的后缀
#     b=oldname[:num]                   #切出文件名的前缀
# newname=b+'[复件]'+a                 #创建新的文件名
# f1=open(oldname,'r')
# f2=open(newname,'w')
# for x in f1.readlines():           #循环读要备份的文件内容并一行一行添加到新的文件里
#     f2.write(x)/

# f1.close()
# f2.close()

# f=open('文件.txt','r')
# a=f.read(5)
# b=f.read(10)
# print(a,b)