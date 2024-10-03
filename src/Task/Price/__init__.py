# Created: 2022.10.12
# Author: Vladimir Vons <VladVons@gmail.com>
# License: GNU, see LICENSE for more details


from .Main import TMain

#Depends = 'Task.Queue'

def Main(_aConf) -> tuple:
    Obj = TMain()
    return (Obj, Obj.Run())
