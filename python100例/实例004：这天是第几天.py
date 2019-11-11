'''
实例004：这天第几天

**题目：**输入某年某月某日，判断这一天是这一年的第几天？

**程序分析：**特殊情况，闰年时需考虑二月多加一天：
'''

def isLeapYear(y):
    return(y%400==0 or (y%4==0 and y%100!=0))
# 定义一个函数,满足上述条件则为闰年
DofM = [0,31,28,31,30,31,30,31,31,30,31,30]
# 记录每个月的日期数
res = 0
year = int(input('Year: '))
if isLeapYear(year):
    print('这是一个闰年，二月将有29天')
else:
    pass
while True:
    month=int(input('Month: '))
    if month >12 :
        print('请输入一个小于12的数字')
    else:
        break
while True:
    day= int(input('day: '))
    if day > 31:
        print('请输入正确的日期')
    else:
        break
if month == 2 and day >28:
    print('您的输入有问题，二月不能超过29天')
if isLeapYear(year):
    DofM[2]+=1
for i in range(month):
    res+=DofM[i]
print(res+day)