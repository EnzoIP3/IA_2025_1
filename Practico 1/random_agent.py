from agent import Agent
<<<<<<< Updated upstream
import random
=======
>>>>>>> Stashed changes


class RandomAgent(Agent):
    def __init__(self):
        pass
<<<<<<< Updated upstream

    def next_action(self, obs):
        direction = random.choice(["R", "L"])
        person1 = random.choice(["A", "B", "C", "D"])
        person2 = random.choice(["A", "B", "C", "D"])

        ret = self.parse_action(direction, person1, person2)

        return ret

    def parse_action(self, direction, person1, person2):
        charToPerson = {"A": 0, "B": 1, "C": 2, "D": 3}

        charToDirection = {
            "R": 1,
            "L": 0,
        }

        d = 0
        p1 = 0
        p2 = 0

        try:
            p1 = charToPerson[person1]
            p2 = charToPerson[person2]
        except Exception:
            print("Unknown person code")

        try:
            d = charToDirection[direction]
        except Exception:
            print("Unknown direction code")

        ret = {"direction": d, "person1": p1, "person2": p2}
        return ret
=======
>>>>>>> Stashed changes
