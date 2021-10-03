# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose, Item


class GildedRoseTest(unittest.TestCase):
    def test_quality_decrease_by_one(self):
        items = [Item("foo", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(9, items[0].quality)

    def test_quality_decrease_by_two_after_sellin(self):
        items = [Item("foo", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_sellin_decreases_but_quality_cannot_be_negative(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
