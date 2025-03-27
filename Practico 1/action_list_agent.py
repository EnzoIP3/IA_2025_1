from agent import Agent
import random


class ActionListAgent(Agent):
    def __init__(self):
        action_list = input("Enter the action list, format is (DPP, ...): ")
        self.action_list = [action.strip() for action in action_list.split(",")]

        if len(self.action_list) < 15:
            raise ValueError("The action list must contain at least 15 actions.")

        self.index = 0
        self.max_index = len(self.action_list)

    def next_action(self, obs):
        if self.index >= self.max_index + 1:
            raise IndexError("No more actions available in the list.")

        direction = self.action_list[self.index][0]
        person1 = self.action_list[self.index][1]
        person2 = self.action_list[self.index][2]
        self.index += 1

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
        except KeyError:
            print("Unknown person code")

        try:
            d = charToDirection[direction]
        except KeyError:
            print("Unknown direction code")

        ret = {"direction": d, "person1": p1, "person2": p2}
        return ret
