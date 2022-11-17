class InvaildRequestView():
    def prepareOutput(self):
        self.addLine("I cannot understand the request you just made!")
        self.addLine("please use `$hockey help` for a list of commands!")