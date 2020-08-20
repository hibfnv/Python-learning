import hashlib


def Enc_paw(r_text, pwd):
    obj = hashlib.md5(r_text)
    obj.update(pwd.encode("utf-8"))
    return obj.hexdigest()


# 利用hashlib动态对md5值对用户输入的密码进行加密，并存储在文本文件中
username = input("Please enter your username: ")
passwd = input("Please enter your password: ")
# 调用函数Enc_paw实现信息加密并写入文件
enc_passwd = Enc_paw(username.encode("utf-8"), passwd)
f = open('userinfo.txt', mode='w', encoding='utf-8')
f.write(username)
f.write("\n")
f.write(enc_passwd)
f.close()
