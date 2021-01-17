#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/15 15:05
# @Author  : Mias
# @File    : demo2.py
'''
练习：发礼物
1.拥有礼物标识
2.定义一个发礼物的方法
3.定义一个展示礼物的方法
4.启动方法
'''
have_gift = False


def send():
    print("发礼物啦")
    global have_gift
    have_gift = True


def show():
    if have_gift == True:
        print("展示礼物")
    else:
        print("没有礼物")


if __name__ == '__main__':
    send()
    show()
