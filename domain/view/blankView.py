from domain.view.view import View
class BlankView(View):
    def prepareOutput(self):
        self.addLine(' ')