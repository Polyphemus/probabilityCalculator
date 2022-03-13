import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, number in kwargs.items():
            for i in range(number):
                self.contents.append(color)

    def draw(self, number):
        draws = []
        if number >= len(self.contents):
            return self.contents
        for i in range(number):
            x = random.randrange(len(self.contents)) # x is a random int between 0 and len of contents
            draws.append(self.contents[x]) # add contents[x] to draws
            self.contents.pop(x) # remote contents[x] from contents
        return draws


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    for i in range(num_experiments):
        expHat = copy.deepcopy(hat)
        expDraw = expHat.draw(num_balls_drawn)
        # if the count of every color in the experimental draw  is greater than the corresponding dictionary value, success
        if all(expDraw.count(k) >= v for k, v in expected_balls.items()):
            successes += 1
    return successes/num_experiments