# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose, Item


class GildedRoseTest(unittest.TestCase):
    def test_item_conjured_decrease_quality_by_2_before_sellin(self):
        items = [Item('Conjured Mana Cake', 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual('Conjured Mana Cake', items[0].name)
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

    def test_item_conjured_decrease_quality_by_4_after_sellin(self):
        items = [Item('Conjured Mana Cake', 0, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual('Conjured Mana Cake', items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)


if __name__ == '__main__':
    unittest.main()
