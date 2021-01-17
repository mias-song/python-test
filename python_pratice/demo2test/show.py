#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/16 14:36
# @Author  : Mias
# @File    : show.py

# import gift
from python_pratice.demo2test import gift


def show():
    if gift.have_gift == True:
        print("展示礼物")
    else:
        print("没有礼物")


print(f"show 的 name值为：{__name__}")
