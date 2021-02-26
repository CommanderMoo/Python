class footClan:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def Chant(self):
        print("ALL HAIL LORD SHREDDER")


footSoldier = footClan("Foot Soldiers", 100, 25)
footTank = footClan("Foot Clan Tanks", 200, 25)
footBrawler = footClan("Brawlers", 100, 50)
