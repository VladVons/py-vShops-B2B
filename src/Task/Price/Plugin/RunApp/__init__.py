# Created: 2024.08.27
# Author: Vladimir Vons <VladVons@gmail.com>
# License: GNU, see LICENSE for more details


import os
import asyncio
import subprocess
#
from Inc.ParserX.Common import TPluginBase
from Inc.Var.Obj import Iif


class TRunApp(TPluginBase):
    async def Run(self):
        App = self.Conf['app']
        if App.startswith('~'):
            App = os.path.expanduser(App)
        Cmd = [App] + self.Conf.get('args', '').split()
        Dir = Iif('/' in App, os.path.dirname(App), None)
        subprocess.Popen(Cmd, cwd=Dir)
        asyncio.sleep(3)
