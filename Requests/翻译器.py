#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests,random,json,tkinter

class YouDaoFanYi(object):
    def __init__(self):
        pass

    def crawl(self, word):
        session = requests.session()
        # 用requests.session()创建session对象，相当于创建了一个特定的会话，帮我们自动保持了cookies。
        agent_list = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400']
        headers = {
            'origin': 'http://fanyi.youdao.com',
            'referer': 'http://fanyi.youdao.com/',
            'user-agent': random.choice(agent_list)
            # 标记了请求从什么设备，什么浏览器上发出，来标识请求的浏览器身份
        }
        data = {
            'i': word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': '15636943022326',
            'ts': '1563694302232',
            'bv': '05435bfabe443fca9224e64675e06aab',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

        res = session.post(url, data=data, headers=headers)
        res_dict = res.json()
        result = res_dict['translateResult'][0][0]['tgt']
        return result

class Application(object):
    def __init__(self):
        self.window = tkinter.Tk()
        self.fanyi = YouDaoFanYi()
        print("当前屏幕的屏幕的宽度为%dpx" % (self.window.winfo_screenwidth()))
        print("当前屏幕的屏幕的高度为%dpx" % (self.window.winfo_screenheight()))
        w, h = self.window.maxsize()
        print(w)
        print(h)
        self.window.title(u'我的翻译')
        # 设置窗口大小和位置
        self.window.geometry('310x370+500+300')
        self.window.minsize(310, 370)
        self.window.maxsize(w, h)
        # 创建一个文本框
        self.result_text1 = tkinter.Text(self.window, background='azure')
        # 喜欢什么背景色就在这里面找哦，但是有色差，得多试试：http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
        self.result_text1.place(x=10, y=5, width=285, height=155)
        self.result_text1.bind("<Key-Return>", self.submit1)

        # 创建一个按钮
        # 为按钮添加事件
        self.submit_btn = tkinter.Button(self.window, text=u'翻译', command=self.submit)
        self.submit_btn.place(x=205, y=165, width=35, height=25)
        self.submit_btn2 = tkinter.Button(self.window, text=u'清空', command=self.clean)
        self.submit_btn2.place(x=250, y=165, width=35, height=25)

        # 翻译结果标题
        self.title_label = tkinter.Label(self.window, text=u'翻译结果:')
        self.title_label.place(x=10, y=165)
        # 翻译结果

        self.result_text = tkinter.Text(self.window, background='light cyan')
        self.result_text.place(x=10, y=190, width=285, height=165)

        # 回车翻译
    def submit1(self, event):
        # 从输入框获取用户输入的值
        content = self.result_text1.get(0.0, tkinter.END).strip().replace("\n", " ")
        # 把这个值传送给服务器进行翻译

        result = self.fanyi.crawl(content)
        # 将结果显示在窗口中的文本框中

        self.result_text.delete(0.0, tkinter.END)
        self.result_text.insert(tkinter.END, result)

        # print(content)

    def submit(self):
        # 从输入框获取用户输入的值
        content = self.result_text1.get(0.0, tkinter.END).strip().replace("\n", " ")
        # 把这个值传送给服务器进行翻译

        result = self.fanyi.crawl(content)
        # 将结果显示在窗口中的文本框中

        self.result_text.delete(0.0, tkinter.END)
        self.result_text.insert(tkinter.END, result)
        print(content)

    # 清空文本域中的内容
    def clean(self):
        self.result_text1.delete(0.0, tkinter.END)
        self.result_text.delete(0.0, tkinter.END)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = Application()
    app.run()