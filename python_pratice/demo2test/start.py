#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/16 14:37
# @Author  : Mias
# @File    : start.py
from python_pratice.demo2test import send, show

if __name__ == '__main__':
    send.send()
    show.show()
    print(f"name值为：{__name__}")
    print(locals())
