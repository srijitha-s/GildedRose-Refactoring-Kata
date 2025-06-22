# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemUpdater:
    def __init__(self, item):
        self.item = item

    def update(self):
        pass

    def increase_quality(self, amount=1):
        self.item.quality = min(50, self.item.quality + amount)

    def decrease_quality(self, amount=1):
        self.item.quality = max(0, self.item.quality - amount)


class DefaultItemUpdater(ItemUpdater):
    def update(self):
        self.decrease_quality()
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.decrease_quality()


class AgedBrieUpdater(ItemUpdater):
    def update(self):
        self.increase_quality()
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.increase_quality()


class BackstagePassUpdater(ItemUpdater):
    def update(self):
        if self.item.sell_in > 10:
            self.increase_quality()
        elif self.item.sell_in > 5:
            self.increase_quality(2)
        elif self.item.sell_in > 0:
            self.increase_quality(3)
        else:
            self.item.quality = 0
        self.item.sell_in -= 1


class SulfurasUpdater(ItemUpdater):
    def update(self):
        # Legendary item: no changes to quality or sell_in
        pass


def get_updater(item):
    if item.name == "Aged Brie":
        return AgedBrieUpdater(item)
    elif item.name == "Backstage passes to a TAFKAL80ETC concert":
        return BackstagePassUpdater(item)
    elif item.name == "Sulfuras, Hand of Ragnaros":
        return SulfurasUpdater(item)
    else:
        return DefaultItemUpdater(item)


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = get_updater(item)
            updater.update()
