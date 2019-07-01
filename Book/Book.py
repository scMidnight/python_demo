#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Book:
    def __init__(self, name, author, comment, state = 0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state

    def __str__(self):
        if self.state == 0:
            # 如果属性state等于0
            status = '未借出'
            # 将字符串'未借出'赋值给status
        else:
            status = '已借出'
        return '名称：《%s》 作者：%s 推荐语：%s 状态：%s ' % (self.name, self.author, self.comment, status)
        # 返回书籍信息

class BookManager:
    __books = []
    def __init__(self):
        book1 = Book('惶然录', '费尔南多·佩索阿', '一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
        book2 = Book('以箭为翅', '简媜', '调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = Book('心是孤独的猎手', '卡森·麦卡勒斯', '我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。', 1)
        self.__books.append(book1)
        self.__books.append(book2)
        self.__books.append(book3)

    def menu(self):
        print('欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地。\n')
        while True:
            print('1.查询所有书籍\n2.添加书籍\n3.借出书籍\n4.归还书籍\n5.退出系统\n')
            choice = int(input('请输入数字选择对应的功能：'))
            if choice == 1:
                self.__show_all_book()
            if choice == 2:
                self.__add_book()
            if choice == 3:
                self.__lend_book()
            if choice == 4:
                self.__return_book()
            if choice == 5:
                print('感谢使用！愿你我成为爱书之人，在茫茫书海中相遇。')
                break
    def __show_all_book(self):
        for book in self.__books:
            # self是实例对象的替身
            print(book)
    def __add_book(self):
        new_name = input('请输入书籍名称：')
        new_author = input('请输入作者：')
        new_comment = input('请输入描述：')
        book = Book(new_name, new_author, new_comment)
        self.__books.append(book)
    def __lend_book(self):
        name = input('请输入你想借阅的书籍名称：')
        res = self.__check_book(name)
        if(res != None):
            if res.state == 1:
                print('你来晚一步，这本书已经被借走了噢')
            else:
                print('借阅成功！借了不看会变胖噢～')
                res.state = 1
        else:
            print('这本书暂时没有收录在系统里呢')
    def __return_book(self):
        name = input('请输入归还书籍的名称：')
        res = self.__check_book(name)
        if(res != None):
            if(res.state == 1):
                res.state = 0
                print('成功归还')
            else:
                print('这本书没有被借走，在等待有缘人的垂青呢！')
        else:
            print('没有这本书噢，你恐怕输错了书名～')
    def __check_book(self, name):
        for book in self.__books:
            if book.name == name:
                return book
        else:
            return None
manager = BookManager()
manager.menu()