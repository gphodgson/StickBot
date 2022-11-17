from domain.view.view import View
class TeamView(View):
    def prepareOutput(self) -> str:
        self.addLine(f'**{self.input.name}**')
        self.addLine(f'Attained {self.input.record.gamesPlayed} points in {self.input.record.gamesPlayed} games this season.')
        self.addLine(f'Record: {self.input.record.wins}-{self.input.record.losses}-{self.input.record.otl}')
