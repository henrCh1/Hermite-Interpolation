# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 14:42:25 2023

@author: 86319
"""

import sympy as sy

def hermite(x, f, df):
    # 声明全局变量
    global X
    # 声明函数变量名为x
    X = sy.symbols('x')
    # 求解四个alpha和beta值
    alpha0 = (1 - (2 * (X - x[0]) / (x[0] - x[1]))) * (((X - x[1]) / (x[0] - x[1])) ** 2)
    alpha1 = (1 - (2 * (X - x[1]) / (x[1] - x[0]))) * (((X - x[0]) / (x[1] - x[0])) ** 2)
    beta0 = (X - x[0]) * (((X - x[1]) / (x[0] - x[1])) ** 2)
    beta1 = (X - x[1]) * (((X - x[0]) / (x[1] - x[0])) ** 2)
    
    # 返回插值多项式
    return f[0] * alpha0 + f[1] * alpha1 + df[0] * beta0 + df[1] * beta1

#初始化数据
x = [1, 2]
f = [2, 3]
df = [1, -1]

#打印插值多项式
print('三次Hermite插值多项式为', sy.simplify(hermite(x, f, df)))