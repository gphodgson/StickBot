from domain.view import View
class BlankView(View):
    def prepareOutput(self):
        self.addLine(' ')