'''
实例001：数字组合
题目：有四个数字1、2、3、4，能组成多少个互不相同且无重复的数字三位数？各是多少
程序分析：遍历全部可以并打印，把有重复的删除
'''
total = 0
for i in range(1,5):
    for j in range(1,5):
        for x in range(1,5):
            if (i!=j)and(j!=x)and(x!=i):
                print(i,j,x)
                total+=1
print(total)

import itertools
sum = 0
a = [1,2,3,4]
for i in itertools.permutations(a,3):
    print(i)
    sum+=1
print(sum)