# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 19:41:27 2021

@author: admin
"""


path = r"C:/Users/admin/Desktop/Python课程项目考察/图书管理系统/用户账号信息.txt"
book_path = r"C:/Users/admin/Desktop/Python课程项目考察/图书管理系统/图书信息.txt"
def user_login():
    """用户登录"""   
    print("欢迎使用图书管理系统！")
    tag = input("已有账号，直接登录？(yes/no)")
    if tag=='yes' or tag=='y' or tag=='Y':
        username = input("请输入用户名：")
        password = input("请输入密码：")
        with open(path, 'rb') as stream:
            result = stream.readlines()
            print(result)
            uesr_list = [i.decode() for i in result]
            for i in uesr_list:
                info = i
                print(info)                
                if username==info[0].rstrip('\r\n') and password==info[1]:
                    print("登录成功")
                    operate(book_path,username)
                    break
                else:
                    print("用户名或密码错误，请重新输入！")
    else:
        print("用户注册")
        user_register()


def user_register():
    """"用户注册"""
    print("欢迎注册图书管理系统！")
    username = input("请输入用户名(6-16位汉字或字母)：")
    with open(path, 'rb') as stream:
            result = stream.readlines()
    if len(username)<6 or len(username)>16:
        print("用户名长度有误！")
    else:
        if username in result:
            print("该用户名已存在，请重新输入！")
        else:
            password = input("请输入密码(不少于6位)：")
            if len(password)<6:
                print("密码位数有误，请重新输入！")
            else:
                password1 = input("请确认密码：")
                if password==password1:
                    print("注册成功！")
                    save_data(path,username,password)
                    login_tag = input("是否登录？(yes/no)")
                    if login_tag=='yes' or login_tag=='y' or login_tag=='Y':
                        user_login()
                    else:
                        pass
                else:
                    print("两次输入的密码不一致，请重新输入！")
                    user_register()


def save_data(file_path,username,password):
    """"保存数据"""
    with open(file_path,'a') as wstream:
        if wstream.writable():
            wstream.writelines('\n')
            wstream.writelines(username)
            wstream.writelines('\n')
            wstream.writelines(password)
        else:
            print("没有权限！")

def person_information(path,username):
    """个人信息的查看和修改""" 
    with open(path) as rstream:
        lines = rstream.readlines()
    tag = input("请选择要进行的操作："+'\n'+"1.查看个人信息"+'\n'+"2.修改个人信息"+'\n')            
    if tag=='1':
        for info in lines:
            info = info.split('   ')
            if username in info:
                print("个人信息:")
                print("用户名：", info[0])
                print("密码：", info[1])
    if tag=='2':
        tag1 = input("请选择要进行的修改操作："+'\n'+"1.修改用户名"+'\n'+"2.修改密码"+'\n')
        if tag1=='1':
            print("用户名不可修改！")
        if tag1=='2':
            new_password = ''
            line = []
            with open(path) as rstream:
                line = rstream.readline()
                if username == line[0]:
                    new_password = input("请输入新密码：")
                    if new_password ==line[1]:
                        print("新密码不能与旧密码相同!")
                    else:
                        line[1] =new_password
            with open(path,'a') as wstream:
                for i in range(len(line)):
                    if i ==0:
                        line[i] = '\n'+line[i]+'\n'
                    else:
                        line[i] = line[i] +'\n'
                wstream.writelines(line)
                print("修改成功") 

             
def find_book(path):
    """查询图书""" 
    with open(path,'r') as rstream:
        books = rstream.readlines()
        book = [books_name for books_name in books]
        for b_name in book:
            print("{}".format(b_name))      
            
            
def permission(user_path,username):
    """管理员"""    
    with open(user_path) as rstream:
        line = rstream.readlines()
        for i in range(len(line)):
            line[i] = line[i].rstrip('\n')
        if username=='admin01':
            pass
        else:
            print("只有管理员admin01才可以进行此操作！")
        operate(path,username)


def add_book(b_path,username):
    """添加图书"""
    permission(b_path,username)
    with open(b_path, 'a') as wstream:
        if wstream.writable:
            book_name = input("请输入书名：")
            with open(b_path) as rstream:
                line = rstream.readlines()
                if book_name in line:
                    print("该书已存在，请勿重复添加！")
                else:
                    book = '\n' + book_name
                    wstream.write(book)
                    print("添加成功!")
        else:
            print("没有权限！")
                
def delete_book(b_path,username):
    """删除图书"""
    permission(path,username)
    with open(b_path, 'r') as rstream:
        book = rstream.read()
        find_book(book_path)
        book_name = input("请输入需要删除的图书书名：")
        for i in range(len(book)-1):
            if book_name == book[i]:
                book.remove(book[i])
    with open(b_path, 'w') as wwstream:
        wwstream.writelines(book)
        print("删除成功！")


def update(b_path,username):
    """修改图书"""
    permission(b_path,username)
    with open(b_path, 'r') as rstream:
        book = rstream.read()
        find_book(book_path)
        book_name = input("请输入需要修改的图书书名：")
        for i in range(len(book)):
            if book_name == book[i]:
                book_name1 = input("请输入修改后的图书书名：")
                book = book_name1 + '\n' 
    with open(b_path, 'w') as wwstream:
        wwstream.writelines(book)
        print("修改成功!")


def borrow_book(username):
    """借书"""
    print("图书列表："+'\n')
    find_book(book_path)
    borrow_book = input("请输入要借的图书书名：")
    with open("C:/Users/admin/Desktop/Python课程项目考察/图书管理系统/已被借走的书.txt") as rstream:
        lines = rstream.readline()
    if borrow_book not in lines:
        if username in lines:
            with open("C:/Users/admin/Desktop/Python课程项目考察/图书管理系统/已被借走的书.txt", 'a') as wstream:
                if borrow_book not in lines:
                    wstream.write("{}".format(borrow_book))
                    print("借书成功!")
                else:
                    print("您已借过此书，请从新选择！")
        else:
            with open("C:/Users/admin/Desktop/Python课程项目考察/图书管理系统/已被借走的书.txt", 'a') as wstream:
                            wstream.write("\n{}:{}\n".format(username, borrow_book))
    else:
        print("该书已被借走，请重新选择！")      
        
def return_book(username):
    """还书"""
    with open("C:/Users/admin/Desktop/Python课程项目考察/图书管理系统/已被借走的书.txt")  as rstream:
        lines = rstream.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].split('，')
            for j in range(len(lines[i])-1):
                if username==lines[i][0]:
                    print("{}您已借阅，未归还图书如下：".format(username))
                    print(lines[i][j+1])
                    return_book = input("请输入您想要归还的书：")
                    with open("C:/Users/admin/Desktop/Python课程项目考察/图书管理系统/已被借走的书.txt") as rstream:
                            lines = rstream.readlines()
                            for i in range(len(lines)):
                                if username in lines[i] and return_book in lines[i]:
                                    lines[i] = lines[i].replace(return_book,'')
                                with open("C:/Users/admin/Desktop/Python课程项目考察/图书管理系统/已被借走的书.txt") as wstream:
                                    wstream.writelines(lines)
                                    print("归还成功！")
                else:
                    print("抱歉，没有找到您的借阅记录！")  


def operate(b_path,username):
    """用户操作页面"""  
    while True:        
        tag = input("请选择要进行的操作："+'\n'+"1.个人信息"+'\n'+"2.查询图书"+'\n'
                +"3.添加图书"+'\n'+"4.删除图书"+'\n'+"5.修改图书"+'\n'+"6.借书"+'\n'
                +"7.还书"+'\n'+"8.退出"+'\n')
        #个人信息
        if tag=='1':
            person_information(path,username)
        #查询图书
        elif tag=='2':
            find_book(path)
        #添加图书
        elif tag=='3':
            add_book(b_path,username)
        #删除图书
        elif tag=='4':
            delete_book(b_path,username)
        #修改图书
        elif tag=='5':
            update(book_path,username)
        #借书
        elif tag=='6':
            borrow_book(username)
        #还书
        elif tag=='7':
            return_book(username)
        #退出
        elif tag=='8':
            tag = input("确定退出登录吗？(yes/no)")
            if tag=='yes' or tag=='y' or tag=='Y':
                print("退出成功！")
                break


#user_login()
operate("C:/Users/admin/Desktop/Python课程项目考察/图书管理系统/图书信息.txt",'AAAAAA')               
                           








