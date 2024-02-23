import asyncio
from IncP.PluginEan import TPluginEan


async def Main():
    PluginEan = TPluginEan('IncP/PluginEan')
    Parser = PluginEan.Load('icecat_biz')
    await Parser.Init()
    Data = await Parser.GetData('57861335')
    pass


asyncio.run(Main())
