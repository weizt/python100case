'''实例005：三数排序

**题目：**输入三个整数x,y,z，请把这三个数由小到大输出。

**程序分析：**练练手就随便找个排序算法实现一下，偷懒就直接调函数。
'''

xyz =[]
x = int(input('请输入一个随意的整数： '))
y = int(input('请输入一个随意的整数： '))
z = int(input('请输入一个随意的整数： '))
xyz.append(x)
xyz.append(y)
xyz.append(z)
print(sorted(xyz))
print(xyz)

raw = []
for i in range(3):
    x = int(input('int%d: ' % (i)))
    raw.append(x)

for i in range(len(raw)):
    for j in range(i, len(raw)):
        if raw[i] > raw[j]:
            raw[i], raw[j] = raw[j], raw[i]
print(raw)

raw2 = []
for i in range(3):
    x = int(input('int%d: ' % (i)))#连续输入三个整数方法
    raw2.append(x)
print(sorted(raw2))