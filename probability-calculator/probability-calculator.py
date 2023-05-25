import copy
import random

class Hat():
    """Hat class"""

    def __init__(self, **balls):
        self.contents = []

        for x in balls.keys():
            self.contents.append(((x + " ") * balls[x]).split())
        self.contents = sum(self.contents, [])


    def draw(self, number):
        """Draw function"""
        contentscopy = copy.deepcopy(self.contents)
        draw = []
        i = 1
        if number > len(contentscopy):
            draw.append(contentscopy)
        else:
            while i <= number:
                rand = random.randrange(0, len(contentscopy))
                draw.append(contentscopy[rand])
                contentscopy.pop(rand)
                i += 1

        return draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    "Probability experiment"
    hatcopy = copy.deepcopy(hat)
    i = 1
    experidraw = []
    expectlist = []
    successes = 0

    for x in expected_balls.keys():
        expectlist.append(((x + " ") * expected_balls[x]).split())
    expectlist = sum(expectlist, [])

    while i <= num_experiments:
       experidraw = hatcopy.draw(num_balls_drawn)
       if experidraw == expectlist: successes += 1

    return successes / num_experiments

hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
