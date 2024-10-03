# Created: 2022.10.14
# Author: Vladimir Vons <VladVons@gmail.com>
# License: GNU, see LICENSE for more details


from Inc.PluginApp import TPluginApp
from Task import App


class TMain():
    async def Run(self, aParam: dict = None):
        Plugin = TPluginApp(f'Conf/{App.Options.get('conf')}')
        Plugin.Init('Task.Price')
        if (isinstance(aParam, dict)):
            for Key, Val in aParam.items():
                Plugin.ConfEx[Key] = Val
        await Plugin.Run()
