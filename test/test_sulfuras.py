# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose, Item


class SulfurasTest(unittest.TestCase):
    def test_item_sulfuras_never_change(self):
        items = [Item('Sulfuras, Hand of Ragnaros', 100, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual('Sulfuras, Hand of Ragnaros', items[0].name)
        self.assertEqual(100, items[0].sell_in)
        self.assertEqual(80, items[0].quality)


if __name__ == '__main__':
    unittest.main()
