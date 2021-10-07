# -*- coding: utf-8 -*-
from typing import List
from item import Item


class GildedRose(List[Item]):
    AGED_BRIE = 'Aged Brie'
    BACKSTAGE_PASSES = 'Backstage passes to a TAFKAL80ETC concert'
    SULFURAS = 'Sulfuras, Hand of Ragnaros'
    CONJURED = 'Conjured Mana Cake'

    def __init__(self, items: List[Item]):
        self.items = items

    def update_quality(self):
        """Updates the quality of every item in Gilded Rose's inventory."""
        for item in self.items:
            self.update_item_quality(item)

    def update_item_quality(self, item: Item):
        """Updates the quality of a specific item in Gilded Rose's
        inventory."""
        after_sellin = item.sell_in < 1
        decrease_quality_value = self._set_decrease_quality_value(item, 
                                                                after_sellin
        )
        quality_should_drop = item.name != self.AGED_BRIE \
                            and item.name != self.BACKSTAGE_PASSES \
                            and item.name != self.SULFURAS
        sellin_should_drop = item.name != self.SULFURAS

        if quality_should_drop:
            self._adjust_quality(item, decrease_quality_value)

        if item.name == self.AGED_BRIE:
            aged_brie_increase_quality_value = 2 if after_sellin else 1
            self._adjust_quality(item, aged_brie_increase_quality_value)

        if item.name == self.BACKSTAGE_PASSES:
            self._handle_backstage_passes_quality(item, after_sellin)

        if sellin_should_drop:
            item.sell_in -= 1

    def _handle_backstage_passes_quality(self, item: Item, 
            after_sellin: bool) -> None:
        """Adjusts the quality of the Backstage Passes item in Gilded Rose's
        inventory."""
        self._adjust_quality(item, 1)
        if item.sell_in < 11:
            self._adjust_quality(item, 1)
        if item.sell_in < 6:
            self._adjust_quality(item, 1)
        if after_sellin:
            item.quality = item.quality - item.quality

    def _set_decrease_quality_value(self, item: Item, 
            after_sellin: bool) -> int:
        """Defines the amount an item should have its quality drop."""
        decrease_quality_value = -2 if item.name == self.CONJURED else -1
        if after_sellin:
            decrease_quality_value *= 2
        return decrease_quality_value
    
    def _adjust_quality(self, item: Item, value: int) -> None:
        """Adjusts item quality if applicable."""
        new_quality = item.quality + value
        should_adjust = True if new_quality >= 0 \
                        and new_quality <= 50 else False
        if should_adjust:
            item.quality = new_quality
