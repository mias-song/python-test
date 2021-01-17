#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 12:01
# @Author  : Mias
# @File    : selectmoney.py

from python_pratice.domo2HomeWork import money


def select():
    if money.saved_money == 1000:
        print("没发工资!")
    else:
        print(f"工资是:{money.saved_money}")
