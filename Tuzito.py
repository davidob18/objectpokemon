from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(30)
        self.spend_attack(40)
        self.spend_defence(30)
        self.add_move(Cabezazo_mortal())
        self.add_move(Mirada_fea())
        self.add_move(Vamos_por_unos_tacos())
        self.add_move(Saca_las_caguamas())
        self.set_type(Type.WATER)
        self.move = 0
        self.moves = ["Mirada fea", "Cabezazo mortal", "Vamos por unos tacos", "Saca las caguamas"]


    def get_name(self):
        return "Tuzito"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class Cabezazo_mortal(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Cabezazo mortal"

class Mirada_fea(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Mirada fea"


class Vamos_por_unos_tacos(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.EARTH)

    def get_name(self):
        return "Vamos por unos tacos"


class Saca_las_caguamas(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Saca las caguamas"
