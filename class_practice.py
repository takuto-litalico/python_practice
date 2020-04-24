
class GunBase():
    def __init__(self, name):
        self.name = name
        self.magsize = 30
        self.d_per_bullet = 35
        self.range = 50
        self.mobility = 50
        self.accuracy = 65
        self.is_semi = True

        self.bullet_remain = self.magsize
    
    def shoot(self):
        self.bullet_remain -= 1
        print("Bang!")
    
    def reload(self):
        self.bullet_remain = self.magsize
        print("Reloaded.")

class AK47(GunBase):
    def __init__(self, name):
        super().__init__(name)
        self.magsize = 33
        self.d_per_bullet = 50
        self.range = 68
        self.mobility = 45
        self.accuracy = 50

    def change_mode(self):
        self.is_semi = not self.is_semi
        if not is_semi:
            self.accuracy = 35
        else:
            self.accuracy = 50

class Player():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self._set_weapons()
        self.is_holding = self.prime_gun

    def _set_weapons(self):
        self.prime_gun = None
        self.second_gun = None
        self.lethal_equip = None
        self.forth_equip = None
    
    def switch_gun(self):
        current_gun = self.is_holding
        if current_gun == self.prime_gun:
            self.is_holding = self.second_gun
        elif current_gun == second_gun:
            self.is_holding = self.prime_gun

gun = GunBase("Tank")

for i in range(1, 11):
    gun.shoot()

print(gun.bullet_remain)

gun.reload()

