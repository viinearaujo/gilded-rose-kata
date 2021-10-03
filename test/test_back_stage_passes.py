# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose, Item


class BackStageTest(unittest.TestCase):
    def test_item_back_stage_increase_quality_by_one_above_sellin_10(self):
        items = [Item('Backstage passes to a TAFKAL80ETC concert', 20, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual('Backstage passes to a TAFKAL80ETC concert', 
                        items[0].name)
        self.assertEqual(19, items[0].sell_in)
        self.assertEqual(3, items[0].quality)

    def test_item_back_stage_increase_quality_by_two_under_sellin_11(self):
        items = [Item('Backstage passes to a TAFKAL80ETC concert', 10, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual('Backstage passes to a TAFKAL80ETC concert', 
                        items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

    def test_item_back_stage_increase_quality_by_three_under_sellin_6(self):
        items = [Item('Backstage passes to a TAFKAL80ETC concert', 5, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual('Backstage passes to a TAFKAL80ETC concert', 
                        items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(5, items[0].quality)

    def test_item_back_stage_quality_zeroed_after_sellin(self):
        items = [Item('Backstage passes to a TAFKAL80ETC concert', 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual('Backstage passes to a TAFKAL80ETC concert', 
                        items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
