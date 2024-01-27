
class roomInfo:
    number:str
    bot:str
    def __init__(self, number):
        self.number=number
        self.bot = []

    def setBot(*bot):
        for x in range(len(bot)):
            bot = bot[x]

    def readNumber(self):
        return self.number

    def readBot(self):
        bots = []
        if len(self.bot) != 0 :
            for x in range(len(self.bot)):
                bots.append(self.bot[x])
        return bots

class rooms(roomInfo):
    #def __init__(self, number):
    #    super.__init__(number)
    #    roomNumber:str = number

    def __init__(self, number, *bot):
        super().__init__(number)
        roomNumber: str = number
        for x in range(len(bot)):
            self.bot = bot[x]
