from mint_price import get_mint_price
from get_curent_price import get_GST

class Shoe:
    def __init__(self, mint_level, rank):
        self.mint_level = mint_level
        self.cooldown = 0
        self.rank = rank

    def mint_level_up(self):
        if self.mint_level < 7:
            self.mint_level += 1

    def increase_cooldown(self):
        self.cooldown += 48

    def mint(self, shoe):
        if self.cooldown > 0 or shoe.cooldown > 0:
            return False
        shoe_1_mint_level = self.mint_level
        shoe_2_mint_level = shoe.mint_level
        summ = shoe_1_mint_level + shoe_2_mint_level
        if summ <= 12:
            self.mint_level_up()
            shoe.mint_level_up()
            self.increase_cooldown()
            shoe.increase_cooldown()

            return Shoe(0, shoe.rank), get_mint_price(self, shoe, get_GST())
        else:
            return False



