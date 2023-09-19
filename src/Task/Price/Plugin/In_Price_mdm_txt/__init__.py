# Created: 2023.05.18
# Author: Vladimir Vons <VladVons@gmail.com>
# License: GNU, see LICENSE for more details


from Inc.ParserX.Common import TPluginBase
from .Main import TProduct


class TIn_Price_mdm_txt(TPluginBase):
    async def Run(self):
        Product = TProduct(self)
        Product.InitEngine()
        await Product.Load()

        return {'TDbCategory': Product.DblCategory, 'TDbProductEx': Product.Dbl}
