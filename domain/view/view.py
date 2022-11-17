class View():
    def __init__(self, input) -> None:
        self.input = input
        self.output = ''

    def addLine(self, string):
        self.output += f'{string}\n'
    
    def addString(self, string):
        self.output += f'{string}'

    def startCodeBlock(self):
        self.output += "\n```\n"

    def endCodeBlock(self):
        self.output += "\n```\n"

    def prepareOutput(self):
        self.addLine("Default Output")

    def createOutput(self) -> str:
        self.prepareOutput()
        return self.output