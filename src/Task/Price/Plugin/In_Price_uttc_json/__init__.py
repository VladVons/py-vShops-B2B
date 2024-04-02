# Created: 2023.07.23
# Author: Vladimir Vons <VladVons@gmail.com>
# License: GNU, see LICENSE for more details

from Inc.Misc.FS import DirWalk
from Inc.DbList import TDbList
from Inc.ParserX.Common import TPluginBase
from .Main import TCategory, TProduct



class TIn_Price_uttc_json(TPluginBase):
    def GetImages(self, aDir: str) -> dict:
        Res = {}
        for (Path, Type, _aDepth) in DirWalk(aDir):
            if (Type == 'f'):
                File = Path.rsplit('/', maxsplit=1)[-1].lower()
                Res[File] = Path
        return Res

    def GetMissedImages(self, aDbl: TDbList, aImages: dict) -> dict:
        Res = []
        for Rec in aDbl:
            Article = Rec.code.lower() + '.jpg'
            if (Article not in aImages):
                Res.append(Rec.code)
                print('-', Rec.code, Rec.name)
            else:
                print('+', Rec.code, Rec.name)
                pass
        return Res

    async def Run(self):
        Category = TCategory(self)
        Engine = Category.InitEngine()
        Category.SetSheet('category')
        await Category.Load()

        Product = TProduct(self)
        Product.InitEngine(Engine)
        Product.SetSheet('product')
        await Product.Load()

        Images = self.GetImages('/home/vladvons/Downloads/ЗІП')
        MissedImages = self.GetMissedImages(Product.Dbl, Images)

        return {'TDbCategory': Category.Dbl, 'TDbProductEx': Product.Dbl}
