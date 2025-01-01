import re
def GetPuzzleInput():
    with open("input21.txt") as file:
        splits = re.findall(r"\d+", file.read())
        hp = splits[0]
        damage = splits[1]
        armor = splits[2]
        return Entity(int(hp), int(damage), int(armor))


class Entity:
    def __init__(self, hp, damage, armor):
        self.hp = hp
        self.damage = damage
        self.armor = armor
    
    def AddStats(self, weapon, armor, rings):
        self.damage += weapon.damage + armor.damage + sum(r.damage for r in rings)
        self.armor += weapon.armor + armor.armor + sum(r.armor for r in rings)

    def Attack(self, enemy):
        enemy.hp -= max(1, self.damage - enemy.armor)
    
    def IsDead(self):
        return self.hp <= 0
    
class Shop:
    def __init__(self, weapons, armors, rings):
        self.weapons = weapons
        self.armors = armors
        self.rings = rings

    def GetCost(self, weapon, armor, rings):
        return weapon.cost + armor.cost + sum(r.cost for r in rings)
        

class Item:
    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

def GetShop():
    weapons = [Item("Dagger", 8, 4, 0), Item("Shortsword", 10, 5, 0), Item("Warhammer", 25, 6, 0), Item("Longsword", 40, 7, 0), Item("Greataxe", 74, 8, 0)]
    armors = [Item("Leather", 13, 0, 1), Item("Chainmail", 31, 0, 2), Item("Splintmail", 53, 0, 3), Item("Bandedmail", 75, 0, 4), Item("Platemail", 102, 0, 5), Item("None", 0, 0, 0)]
    rings = [Item("Damage +1", 25, 1, 0), Item("Damage +2", 50, 2, 0), Item("Damage +3", 100, 3, 0), Item("Defense +1", 20, 0, 1), Item("Defense +2", 40, 0, 2), Item("Defense +3", 80, 0, 3), Item("None", 0, 0, 0), Item("None2",0,0,0)]
    return Shop(weapons, armors, rings)

def GetPossibleCombos(shop: Shop):
    for weapon in shop.weapons:
        for armor in shop.armors:
            for ring1 in shop.rings:
                for ring2 in shop.rings:
                    if ring1 == ring2:
                        continue
                    yield (weapon, armor, ring1, ring2)

def GetCheapestWinningCombo(shop):
    winningCombos = []
    for combo in GetPossibleCombos(shop):
        player = Entity(100, 0, 0)
        boss = GetPuzzleInput()
        player.AddStats(combo[0], combo[1], [combo[2], combo[3]])
        boss.AddStats(Item("Boss", 0, 0, 0), Item("Boss", 0, 0, 0), [])
        while not player.IsDead() and not boss.IsDead():
            player.Attack(boss)
            if boss.IsDead():
                winningCombos.append((shop.GetCost(combo[0], combo[1], [combo[2], combo[3]])))
                break
            boss.Attack(player)
    return min(winningCombos)

def GetMostExpensiveLosingCombo(shop):
    losingCombos = []
    for combo in GetPossibleCombos(shop):
        player = Entity(100, 0, 0)
        boss = GetPuzzleInput()
        player.AddStats(combo[0], combo[1], [combo[2], combo[3]])
        boss.AddStats(Item("Boss", 0, 0, 0), Item("Boss", 0, 0, 0), [])
        while not player.IsDead() and not boss.IsDead():
            player.Attack(boss)
            if boss.IsDead():
                break
            boss.Attack(player)
        if player.IsDead():
            losingCombos.append((shop.GetCost(combo[0], combo[1], [combo[2], combo[3]])))
    return max(losingCombos)

print(GetCheapestWinningCombo(GetShop()))
print(GetMostExpensiveLosingCombo(GetShop()))