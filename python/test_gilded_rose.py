# -*- coding: utf-8 -*-

import unittest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_normal_item_before_sell_date(self):
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)

    def test_normal_item_on_sell_date(self):
        items = [Item("Normal Item", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(18, items[0].quality)

    def test_normal_item_quality_never_negative(self):
        items = [Item("Normal Item", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_increases_quality(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)
        self.assertEqual(1, items[0].sell_in)

    def test_aged_brie_quality_max_50(self):
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_does_not_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_backstage_pass_increase_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_backstage_pass_increase_2_when_10_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(27, items[0].quality)

    def test_backstage_pass_increase_3_when_5_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(28, items[0].quality)

    def test_backstage_pass_quality_drops_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
