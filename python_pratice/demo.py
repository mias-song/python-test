#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 19:52
# @Author  : name
# @File    : demo.py
a = 1


def fun():
    global a
    a = 2
    print(id(a))
    print(f"这是一个方法:a={a}")


print(a)
print(id(a))
fun()
print(a)
print(id(a))
print(fun())
if __name__ == '__main__':
    print("start")
    fun()
    print("end")
