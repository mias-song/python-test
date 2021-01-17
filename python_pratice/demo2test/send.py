#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/16 14:35
# @Author  : Mias
# @File    : send.py

# import gift
from python_pratice.demo2test import gift


def send():
    print("发礼物啦")
    gift.have_gift = True


print(f"send 的 name值为：{__name__}")
