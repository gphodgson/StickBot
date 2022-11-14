from domain.view import View

class TeamsView(View):

    def prepareOutput(self) -> None:
        self.addLine("**NHL Teams:**")
        self.startCodeBlock()
        for team in self.input:
            self.addLine(f'{team.name}: {team.id}')
        self.endCodeBlock()