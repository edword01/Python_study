#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
############### 检测程序运行时间 ####################
##(带参数)装饰器练习
import datetime,functools,time
def ProgramRunningTime(*para):       #para为可选参数
    def f(p_function):
    #经过装饰器修饰后的函数_name_属性变成了wrapper，下面这行实现wrapper._name_=p_function._name_
        @functools.wraps(p_function)
        def wrapper(*args,**kw):
            start_time=datetime.datetime.now()
            #print('start time:',start_time)
            p_function(*args,**kw)
            end_time=datetime.datetime.now()
            total=end_time-start_time
            if len(para)>0:
                print('%s(...) Function RunningTime:%f %s' %(*para,total.total_seconds(),'秒'))
            else:
                print('XXX Function RunningTime:%f %s' %(total.total_seconds(),'秒'))
        return wrapper

    return f
##############################################################
