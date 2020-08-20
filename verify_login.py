import hashlib


def Enc_passwd(r_text, pawd):
    obj = hashlib.md5(r_text)
    obj.update(pawd.encode("utf-8"))
    return obj.hexdigest()


# 对用户输入的信息与自身文本进行匹配，如果匹配成功则表示用户输入正确，如果错误则需要用户重新输入，一直到用户输入正确。
# 定义用户输入函数
username = input("请输入用户名：")
user_passwd = input("请输入用户密码: ")
# 判断用户输入，并对用户输入的密码与存储信息比对。
user_passwd = Enc_passwd(username.encode("utf-8"), user_passwd)
f = open('userinfo.txt', mode='r', encoding='utf-8')
username1 = f.readline().strip()
user_passwd1 = f.readline().strip()
while username != username1 and user_passwd != user_passwd1:
    print("\033[31m输入信息有误，请重新输入。\033[0m")
else:
    print("\033[33m用户信息匹配，输入正确。\033[0m")


