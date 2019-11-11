#### 实例007：copy

#**题目：**将一个列表的数据复制到另一个列表中。

#**程序分析：**使用列表[:]，拿不准可以调用copy模块。
list1 = [0,1,2,3,4,5,6,7,8,9]

list2 =[]
for i in list1:
    list2.append(i)
print(list2)

list3 = list1[:]
print(list3)
