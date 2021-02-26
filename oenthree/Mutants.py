class Monsters:
    def __init__(self, health, speed):
        self.health = health
        self.speed = speed

    def talk(self, chatter):
        print(chatter)


MonsterOne = Monsters(50, 5)
MonsterRanged = Monsters(75, 10)
MonsterBoss = Monsters(100, 5)