# Created: 2023.02.08
# Author: Vladimir Vons <VladVons@gmail.com>
# License: GNU, see LICENSE for more details


from Inc.ParserX.Parser_dbl import TParser_dbl
from ..CommonDb import TDbCategory, TDbProductEx


class TCategory(TParser_dbl):
    def __init__(self, aParent):
        super().__init__(aParent, TDbCategory())

    def _Fill(self, aRow):
        Rec = self.Dbl.RecAdd()

        for x in ['id', 'parent_id', 'name']:
            self.Copy(x, aRow, Rec)


class TProduct(TParser_dbl):
    def __init__(self, aParent):
        super().__init__(aParent, TDbProductEx())

    def _Fill(self, aRow):
        Rec = self.Dbl.RecAdd()

        Xlat = [
            ['article', 'stock_quantity', 'price_dealer', 'manufacturer_name'],
            ['code',    'qty',            'price_in',     'vendor']
        ]
        for xSrc, xDst in zip(*Xlat):
            self.CopyAs(xSrc, xDst, aRow, Rec)

        for x in ['id', 'category_id', 'name', 'descr']:
            self.Copy(x, aRow, Rec)
