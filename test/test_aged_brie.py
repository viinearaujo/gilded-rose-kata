# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose, Item


class AgedBrieTest(unittest.TestCase):
    def test_item_aged_brie_increase_quality_by_one_the_older_it_gets(self):
        items = [Item('Aged Brie', 2, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual('Aged Brie', items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(3, items[0].quality)

    def test_item_aged_brie_increase_quality_by_two_after_sellin(self):
        items = [Item('Aged Brie', 0, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual('Aged Brie', items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

    def test_item_aged_brie_wont_go_above_max_quality_50(self):
        items = [Item('Aged Brie', 2, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual('Aged Brie', items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(50, items[0].quality)


if __name__ == '__main__':
    unittest.main()
