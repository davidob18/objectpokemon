from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(0)
        self.spend_attack(0)
        self.spend_defence(100)
        self.add_move(Chancla_fuego())
        self.add_move(Escupir())
        self.add_move(Taco_picante())
        self.add_move(Agua_horchata())
        self.set_type(Type.FIRE)
        self.move = 0
        self.moves = ['Taco picante!!', "Escupitajo", "Agua de horchata!", "Chancla de fuego"]


    def get_name(self):
        return "Xolojolote"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class Chancla_fuego(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Chancla de fuego"

class Escupir(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Escupitajo"


class Taco_picante(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Taco picante!!"


class Agua_horchata(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Agua de horchata!"
