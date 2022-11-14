from domain.view import View
class JoinChannelView(View):
    def prepareOutput(self):
        self.addLine("Please join a channel before requesting a song.")