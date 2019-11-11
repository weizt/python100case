'''
实例006：斐波那契数列

**题目：**斐波那契数列。

**程序分析：**斐波那契数列（Fibonacci sequence），从1,1开始，后面每一项等于前面两项之和。图方便就递归实现，
图性能就用循环。
'''
#第一种方法：(递归实现)
def Value(n):
    return 1 if n <=2 else Value(n-1) + Value(n-2)
print(Value(int(input('请输入一个数字： '))))

#第二种方法：（朴素实现）
target=int(input('请输入一个数字： '))
res=0
a,b=1,1
for i in range(target-1):
    a,b=b,a+b
print(a)

#第三种方法
value = int(input('请输入一个数字： '))
a = 0
b = 1
while b < value:
    print(b)
    a = b
    b = a+b
