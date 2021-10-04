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
    CONJURED = 'Conjured Mana Cake'

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item_quality(item)

    def update_item_quality(self, item):
        after_sellin = item.sell_in < 1
        decrease_quality_value = self._set_decrease_quality_value(item, after_sellin)
        quality_should_drop = item.name != self.AGED_BRIE \
                            and item.name != self.BACKSTAGE_PASSES \
                            and item.name != self.SULFURAS

        if quality_should_drop:
            self._adjust_quality(item, decrease_quality_value)

        if item.name == self.AGED_BRIE:
            self._adjust_quality(item, 1)

        if item.name == self.BACKSTAGE_PASSES:
            self._adjust_quality(item, 1)
            if item.sell_in < 11:
                self._adjust_quality(item, 1)
            if item.sell_in < 6:
                self._adjust_quality(item, 1)

        if item.name != self.SULFURAS:
            item.sell_in = item.sell_in - 1

        if after_sellin:
            if item.name == self.AGED_BRIE:
                self._adjust_quality(item, 1)
            else:
                if item.name == self.BACKSTAGE_PASSES:
                    item.quality = item.quality - item.quality

    def _set_decrease_quality_value(self, item: Item, after_sellin: bool) -> int:
        decrease_quality_value = -2 if item.name == self.CONJURED else -1
        if after_sellin:
            decrease_quality_value *= 2
        return decrease_quality_value
    
    def _adjust_quality(self, item: Item, value: int) -> None:
        new_quality = item.quality + value
        should_adjust = True if new_quality >= 0 and new_quality <= 50 else False
        if should_adjust:
            item.quality = new_quality



