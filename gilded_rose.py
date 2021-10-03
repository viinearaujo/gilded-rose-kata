# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):
    AGED_BRIE = 'Aged Brie'
    BACKSTAGE_PASSES = 'Backstage passes to a TAFKAL80ETC concert'
    SULFURAS = 'Sulfuras, Hand of Ragnaros'

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item_quality(item)

    def update_item_quality(self, item):
        if item.name != self.AGED_BRIE and item.name != self.BACKSTAGE_PASSES:
                if item.quality > 0:
                    if item.name != self.SULFURAS:
                        self._adjust_quality(item, -1)
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if item.name == self.BACKSTAGE_PASSES:
                    if item.sell_in < 11:
                        if item.quality < 50:
                            self._adjust_quality(item, 1)
                    if item.sell_in < 6:
                        if item.quality < 50:
                            self._adjust_quality(item, 1)
        if item.name != self.SULFURAS:
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.name != self.AGED_BRIE:
                if item.name != self.BACKSTAGE_PASSES:
                    if item.quality > 0:
                        if item.name != self.SULFURAS:
                            self._adjust_quality(item, -1)
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    self._adjust_quality(item, 1)
    
    def _adjust_quality(self, item: Item, value: int):
        item.quality += value



