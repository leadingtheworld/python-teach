def center_c(res,long):
    return res.center(long,'-')
res,long,="注册",20
res1=center_c(res,long)
print(res1)
username = input("请输入你要注册的账号>>>>").strip()
password = input("请输入你要注册的密码>>>>").strip()
while True:
    number = input("请输入你要注册的电话号码>>>").strip()
    if len(number)==11 and number.isdigit():
            with open('data/userpass.txt', mode='at', encoding='utf-8') as f:
                f.write(f'{username}----{password}----{number}\n')
            break
    else:
        print('请输入11位电话号码或是不要包含其他符号')
        print("请重新输出电话号码>>>")
        continue

print('-' * 10, '登录', '-' * 10)
user_name = input("请输入你要登录的账号>>>>").strip()
pass_word = input("请输入你要登录的密码>>>>").strip()
with open('data/userpass.txt',mode='rt',encoding='utf-8') as f2:
    res_1=f2.read()
    dic={}
    for line in res_1:
        username,password=line.strip().split("----")
        dic[username]=password
num_ber=0
while num_ber<5:
    if user_name==username and pass_word==password:
        print("登录成功")
        while True:
            n_um=input("请输入你的操作")
            print(f'正在{n_um}')
            if n_um=='exit':
                print('正在退出程序')
            break
        break
    else:
        print('账号或者密码错误,请重新输入')
        num_ber += num_ber + 1

else:
    print('已经错误了5次,请明天再尝试把')
