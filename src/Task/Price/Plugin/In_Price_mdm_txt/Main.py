# Created: 2023.09.18
# Author: Vladimir Vons <VladVons@gmail.com>
# License: GNU, see LICENSE for more details
#
# '5x Monitor  LCD 22" ViewSonic VG2239SMH  150 zł netto/szt.'
# '3x DELL 7390 i5-8350U 8GB 256SSD W10P COA FHD TOUCH -  150 zł netto/szt.''
# '5x DELL 5070 SFF I5-9500 8GB 256SSD RW W10P COA BOX 150 zł netto/szt.''
# '1x DELL PREC 5810 E5-1650v3 32GB 1TB RW K2200 COA 150 zł netto/szt.''


import re
#
from Inc.Util.Str import ToFloat
from Inc.ParserX.Parser_txt import TParser_txt
from IncP.Log import Log
from ..CommonDb import TDbCategory, TDbProductEx


class TProduct(TParser_txt):
    def __init__(self, aParent):
        super().__init__(aParent, TDbProductEx())

        self.ReBody = re.compile(r'(\d+)\s*x\s*(.*?)[\s-]*(\d+)\s*z', re.IGNORECASE)
        self.ReMonit = re.compile(r'(\d*)\"\s*(.*?)$', re.IGNORECASE)
        self.ReMonitDel = re.compile(r'Monitor LCD \d+"\s', re.IGNORECASE)
        self.ReComputer = re.compile(r'(.*?)\s*(\d*x?[ie]\d+-\w+)\s*(\d+GB)\s*(\d+\w+)', re.IGNORECASE)

        self.Category = {'Компютер': 1, 'Монітор': 2, 'Ноутбук': 3}
        self.DblCategory = TDbCategory()
        for Key, Val in self.Category.items():
            self.DblCategory.RecAdd().SetAsDict({'id': Val, 'parent_id': 0, 'name': Key})

    def _Fill(self, aRow: dict):
        Data = aRow['data']
        if (not Data.strip()):
            return

        MatchBody = self.ReBody.findall(Data)
        if (not MatchBody):
            return

        Qty, Body, Price = MatchBody[0]
        if ('Monitor' in Body):
            CategoryId = self.Category['Монітор']
            Matches = self.ReMonit.findall(Body)
            if (Matches):
                Model = Matches[0][1]
                Body = self.ReMonitDel.sub('', Body)
        elif any(s in Body for s in [' HD', ' FHD', ' QHD']):
            CategoryId = self.Category['Ноутбук']
            Matches = self.ReComputer.findall(Body)
            if (Matches):
                Model = f'{Matches[0][0]} {Matches[0][1]}'
        else:
            CategoryId = self.Category['Компютер']
            Matches = self.ReComputer.findall(Body)
            if (Matches):
                Model = f'{Matches[0][0]} {Matches[0][1]}'

        if (Matches):
            self.Dbl.RecAdd().SetAsDict({
                'category_id': CategoryId,
                'code': Model.lower(),
                'name': Body,
                'price_in': ToFloat(Price),
                'qty': int(Qty)
                })
            self.Dbl.Rec.Flush()
        else:
            Log.Print(1, 'i', f'Parser err: {Body}')
