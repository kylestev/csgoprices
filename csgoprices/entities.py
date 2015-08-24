class Wear(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Wears(object):
    WellWorn = Wear('Well-Worn')
    FactoryNew = Wear('Factory New')
    FieldTested = Wear('Field-Tested')
    MinimalWear = Wear('Minimal Wear')
    BattleScarred = Wear('Battle-Scarred')


class Skin(object):
    def __init__(self, gun, name, wear, knife=False, stattrak=False):
        self.gun = gun
        self.name = name
        self.wear = wear
        self.knife = knife
        self.stattrak = stattrak

    def __str__(self):
        return '{} | {} ({})'.format(self.gun, self.name, self.wear)
