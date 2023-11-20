"""File to define River class."""
__author__ = "730577037"
from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Create River Class and define attributes."""
    day: int
    fish: list
    bears: list

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of animals."""
        surviving_f = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_f.append(fish)
        self.fish = surviving_f
        surviving_b = []
        for bear in self.bears:
            if bear.age <= 5:
                surviving_b.append(bear)
        self.bears = surviving_b

    def remove_fish(self, amount: int):
        """Removes the fish from the front of the list."""
        for fish in range(amount):
            if self.fish:
                self.fish.pop(0)
        return None  
    
    def bears_eating(self):
        """Calculates the bears eating and removes accordingly."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3) 
                bear.eat(3)
        return None

    def check_hunger(self):
        """Finds and removes the bears that are hungry."""
        new_b = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_b.append(bear)
        self.bears = new_b
        return None
    
    def repopulate_fish(self):
        """Repopulation of the fish."""
        baby_f = []
        num_new_fish = (len(self.fish) // 2)
        for i in range(num_new_fish):
            baby_f += [Fish()] * 4
        self.fish += baby_f
        return None

    def repopulate_bears(self):
        """Repopulation of the bears."""
        baby_b = []
        num_new_bears = len(self.bears) // 2
        for i in range(num_new_bears):
            baby_b.append(Bear())
        self.bears += baby_b

    def view_river(self):
        """Prints the day, fish population, and bear population."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates one week."""
        for i in range(7):
            self.one_river_day()    