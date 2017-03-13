# -*- coding=utf-8 -*-
from utiltool.DBOperator import MSSQL
from LogModule import setup_logging


import logging

setup_logging()
logger = logging.getLogger(__name__)

#为了使连接池只初始化一次创建此处2个全局变量，因为涉及别人的代码，导致设计上有出入，造成了circular dependency between the modules
#所以此处新建了一个专门管理数据库的全局变量
class GlobalParams1(object):
    ms = MSSQL()


def init():
    pass


def GetSqlCluster():
    return GlobalParams1.ms






