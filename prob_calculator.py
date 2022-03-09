import copy
import random
# Consider using the modules imported above.


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
            x = random.randrange(len(self.contents))
            draws.append(self.contents[x])
            self.contents.pop(x)
        return draws


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    for i in range(num_experiments):
        expHat = copy.deepcopy(hat)
        expDraw = expHat.draw(num_balls_drawn)
        if all(v >= expDraw.count(k) for k, v in expected_balls.items()):
            successes += 1
    return successes/num_experiments

## use small numbers of experiments, print out results