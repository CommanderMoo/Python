from abc import ABC, abstractmethod

# polymorphism
# class with multiple functions but no implementations
# inheritance
# create a class to derive from another
# abstraction


class Place(ABC):
    def __init__(self, location, state, teams):
        self.location = location
        self.state = state
        self.teams = teams
# self.location = str(location())

    @abstractmethod
    def Location(self):
        return "Welcome to " + self.location

    @abstractmethod
    def State(self):
        return "Welcome to " + self.state

    @abstractmethod
    def SportsTeam(self):
        return "We should check out the" + self.teams


class LA(Place):
    def __init__(self):
        Place.__init__(self, "Los Angelos", "East Coast", "LA Lakers")

    def Location(self):
        super().Location()

    def State(self):
        super().State()

    def SportsTeam(self):
        super().SportsTeam()


class Houston(Place):
    def __init__(self):
        Place.__init__(self, "Houston", " LoanStar ", "Houston Rockets")

    def Location(self):
        super().Location()

    def State(self):
        super().State()

    def SportsTeam(self):
        super().SportsTeam()


class WashingtonDC(Place):
    def __init__(self):
        # lol ill fix those later
        super().__init__("Washington", "Capital", "Who knows")

    def Location(self):
        super().Location()

    def State(self):
        super().State()

    def SportsTeam(self):
        super().SportsTeam()




