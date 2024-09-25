#Created:     2022.04.30
#Author:      Vladimir Vons <VladVons@gmail.com>
#License:     GNU, see LICENSE for more details


import os
import sys
import platform


__version__ = '1.0.1'
__date__ =  '2023.07.27'


def GetAppVer() -> dict:
    return {
        'app_name' : 'vShops-B2B',
        'app_ver' : __version__,
        'app_date': __date__,
        'author':  'Vladimir Vons, VladVons@gmail.com',
        'home': 'http://oster.com.ua',
    }
