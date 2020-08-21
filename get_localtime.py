# 此脚本为一个简单不带任何判断的时间转换小程序，主要是项固自身对于datetime模块中strftime和strptime以及now()获取时间的运用。
from datetime import datetime


def today():
    t_date = datetime.now()
    ct_time = datetime.strftime(t_date, '%Y年%m月%d日 %H时%M分%S秒')
    print("今天的时间是: " + ct_time)


# 通过判断用户获得的数据来进行信息交互，以实现对用户数据的格式转换
def user_input():
    s = input("请输入你想转换的时间(格式为YYYY/MM/DD HH:MM:SS): ")
    gt_time = datetime.strptime(s, '%Y/%m/%d %H:%M:%S')
    ct1_time = datetime.strftime(gt_time, '%Y年%m月%d日 %H时%M分%S秒')
    print("您输入的时间是: " + ct1_time)


today()
user_input()
