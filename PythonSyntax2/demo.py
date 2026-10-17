class Footballplayer:
    def __init__(self, club, skill, position):
        self.club = club
        self.skill = skill
        self.position = position

    def show_details(self):
        print("Club:", self.club)
        print("Skill:", self.skill)
        print("Position:", self.position)


class Striker(Footballplayer):
    def __init__(self, club, skill, position, goals):
        super().__init__(club, skill, position)
        self.goals = goals

    def show_striker_details(self):
        self.show_details()  
        print("Goals Scored:", self.goals)


player1 = Striker("Barcelona", "Finishing", "Striker", 35)

player1.show_striker_details()
