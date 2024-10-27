# A base class for TTRPG PCs / Monsters
class actor:
    def __init__(self):
        self.actions = 3
        self.reactions = 1
        self.hpMax = 10
        self.hp = self.hpMax
        self.AC = 13
    
    def regainActions():
        self.actions = 3
        self.reactions = 1

    def TurnStart():
        regainActions()

    def CheckHit(self,attackRoll):
        return strikeHit(self.AC,attackRoll)
    
    def TakesDamage(self,damage):
        self.hp -= damage