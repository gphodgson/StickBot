from domain.view.view import View

class StopPlayingView(View):
    def prepareOutput(self):
        self.addLine("Stopped playing music.")