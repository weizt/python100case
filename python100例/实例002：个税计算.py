'''实例002：“个税计算”

题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，
可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时
高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

程序分析：分区间计算即可。
'''

'''
def test(profile):
    #    while True:
    if profile > 0 and profile <= 100000:
        bonus = profile * 0.1
        print(bonus)
    elif profile > 100000 and profile <= 200000:
        bonus = 100000 * 0.1 + (profile - 100000) * 0.075
        print(bonus)
    elif profile > 200000 and profile <= 400000:
        bonus = 100000 * 0.1 + 100000 * 0.075 + (profile - 200000) * 0.05
        print(bonus)
    elif profile > 400000 and profile <= 600000:
        bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + (profile - 400000) * 0.03
        print(bonus)
    elif profile > 600000 and profile <= 1000000:
        bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + (profile - 600000) * 0.015
        print(bonus)
    elif profile > 1000000:
        bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + (
                    profile - 600000) * 0.01
        print(bonus)
    #        elif profile == 0:
    #            break


def main():
    profile = 1
    while profile != 0:
        profile = int(input('请输入利润/元'))
        test(profile)

main()
'''




profit=int(input('Show me the money: '))
bonus = 0
thresholds=[100000,100000,200000,200000,400000]
rates=[0.1,0.075,0.05,0.03,0.015,0.01]
for i in range(len(thresholds)):
    if profit<=thresholds[i]:
        bonus+=profit*rates[i]
        profit=0
        break
    else:
        bonus+=thresholds[i]*rates[i]
        profit-=thresholds[i]
bonus+=profit*rates[-1]
print(bonus)


money = int(input('请输入金额：' ))
thresholds = [100000,100000,200000,200000,400000]
tatio = [0.1,0.075,0.05,0.03,0.015,0.01]
bonus = 0
for i in range(len(thresholds)):
    if i <=thresholds[i]:
        bonus += money * tatio[i]
        money = 0
        break
    else:
        bonus += thresholds[i]*tatio[i]
        money -=thresholds[i]
bonus = money*tatio[-1]
print(bonus)
