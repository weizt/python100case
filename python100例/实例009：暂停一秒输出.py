#### 实例009：暂停一秒输出

#**题目：**暂停一秒输出。

#**程序分析：**使用 time 模块的 sleep() 函数。
import time
a = '这是一段文字，用来测试暂停一秒输出'
for i in a:
    print(i,end = '')
    time.sleep(1)


import time
for i in range(4):
    print(str(int(time.time()))[-2:])
    time.sleep(1)