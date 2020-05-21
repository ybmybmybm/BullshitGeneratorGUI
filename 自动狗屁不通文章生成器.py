#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, re
import tkinter as tk
import random,readJSON

data = readJSON.读JSON文件("data.json")
名人名言 = data["famous"] # a 代表前面垫话，b代表后面垫话
前面垫话 = data["before"] # 在名人名言前面弄点废话
后面垫话 = data['after']  # 在名人名言后面弄点废话
废话 = data['bosh'] # 代表文章主要废话来源

original_str = "学生会退会"

重复度 = 2

def 洗牌遍历(列表):
    global 重复度
    池 = list(列表) * 重复度
    while True:
        random.shuffle(池)
        for 元素 in 池:
            yield 元素

下一句废话 = 洗牌遍历(废话)
下一句名人名言 = 洗牌遍历(名人名言)

def 来点名人名言():
    global 下一句名人名言
    original_str = next(下一句名人名言)
    original_str = original_str.replace(  "a",random.choice(前面垫话) )
    original_str = original_str.replace(  "b",random.choice(后面垫话) )
    return original_str

def 另起一段():
    xx = ". "
    xx += "\r\n"
    xx += "    "
    return original_str



class Translate():
    def __init__(self):
        self.window = tk.Tk()  #创建window窗口
        self.window.title("文章生成器")  # 定义窗口名称
        self.window.resizable(0,0)  # 禁止调整窗口大小
        self.input = tk.Entry(self.window, width=80)  # 创建一个输入框,并设置尺寸
        self.info = tk.Text(self.window, height=18)   # 创建一个文本展示框，并设置尺寸
        # 添加一个按钮，用于触发翻译功能
        self.t_button = tk.Button(self.window, text='生成', relief=tk.RAISED, width=8, height=1, command=self.start)
        # 添加一个按钮，用于触发清空输入框功能
        self.c_button1 = tk.Button(self.window, text='清空输入', relief=tk.RAISED, width=8, height=1, command=self.cle_e)
        # 添加一个按钮，用于触发清空输出框功能
        self.c_button2 = tk.Button(self.window, text='清空输出', relief=tk.RAISED,width=8, height=1, command=self.cle)

    def gui_arrang(self):
        """完成页面元素布局，设置各部件的位置"""
        self.input.grid(row=0,sticky="W",padx=1)
        self.info.grid(row=1)
        self.t_button.grid(row=0,column=1,padx=2)
        self.c_button1.grid(row=0, column=2, padx=2)
        self.c_button2.grid(row=0,column=3,padx=2)

    def start(self):
        """定义一个函数，完成功能"""
        original_str = self.input.get()  # 定义一个变量，用来接收输入框输入的值
        data = {
            'doctype': 'json',
            'type': 'AUTO',
            'i': original_str  # 将输入框输入的值，赋给接口参数
        }
        for x in original_str:
            tmp = str()
            while ( len(tmp) < 6000 ) :
                分支 = random.randint(0,100)
                if 分支 < 5:
                    tmp += 另起一段()
                elif 分支 < 20 :
                    tmp += 来点名人名言()
                else:
                    tmp += next(下一句废话)
            tmp = tmp.replace("x",original_str)
        self.info.delete(1.0, "end")  # 输出内容前，先清空输出框的内容
        self.info.insert('end',tmp)  # 将结果添加到输出框中

    def cle(self):
        """定义一个函数，用于清空输出框的内容"""
        self.info.delete(1.0,"end")  # 从第一行清除到最后一行

    def cle_e(self):
        """定义一个函数，用于清空输入框的内容"""
        self.input.delete(0,"end")


def main():
    t = Translate()
    t.gui_arrang()
    tk.mainloop()

if __name__ == "__main__":
    main()
