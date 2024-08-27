# Created: 2023.06.22
# Author: Vladimir Vons <VladVons@gmail.com>
# License: GNU, see LICENSE for more details


from Inc.ParserX.Parser_xlsx import TParser_xlsx
from ..CommonDb import TDbCrawl


class TMain(TParser_xlsx):
    def __init__(self, aParent):
        super().__init__(aParent, TDbCrawl())

    def _Fill(self, aRow: dict):
        aCode = aRow['code']
        if (aRow['model'] and aCode):
            if (isinstance(aCode, str)):
                aCode = aCode.strip()
            else:
                aCode = str(int(aCode))

            if (len(aCode) >= 4):
                Rec = self.Dbl.RecAdd()
                Rec.SetField('code', aCode)
                for x in ['tenant', 'category', 'model', 'url']:
                    self.Copy(x, aRow, Rec)

                Rec.Flush()
