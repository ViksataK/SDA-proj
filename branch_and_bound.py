from item import Item
from settings import MAX_WEIGHT
max_weight = MAX_WEIGHT


def sorted_(items):
    return sorted(items, key=lambda item: item.get_efficiency(), reverse=True)


class UpperBound:
    def __init__(self, items, level=0, benefit=0, weight=0, taken=[]):
        self.items = items
        self.level = level
        self.benefit = benefit
        self.weight = weight
        self.taken = taken
        self.available = self.taken[:self.level] + [1] * (len(items) - level)
        self.upperbound = self.calctulate_upperbound()

    def calctulate_upperbound(self):
        upperbound = 0
        weight_accumulate = 0
        for i in range(len(self.items)):
            if self.items[i].get_weight() * self.available[i] <= max_weight - weight_accumulate:
                weight_accumulate += self.items[i].get_weight() * self.available[i]
                upperbound += self.items[i].get_value() * self.available[i]
            else:
                upperbound += self.items[i].get_value() * (
                    max_weight - weight_accumulate) / self.items[i].get_weight() * self.available[i]
                break
        return upperbound

    def develop(self):
        level = self.level + 1
        if self.weight + self.items[self.level].get_weight() <= max_weight:
            left_weight = self.weight + self.items[self.level].get_weight()
            left_benefit = self.benefit + self.items[self.level].get_value()
            left_taken = self.taken[:self.level] + \
                [1] + self.taken[self.level + 1:]
            left_child = UpperBound(
                self.items, level, left_benefit, left_weight, left_taken)
        else:
            left_child = None
        right_child = UpperBound(
            self.items, level, self.benefit, self.weight, self.taken)
        if left_child is not None:
            return [left_child, right_child]
        else:
            return [right_child]


def execute(items):
    items = sorted_(items)
    Root = UpperBound(items, 0, 0, 0, [0] * len(items))
    waiting_States = []
    current_state = Root
    while current_state.level < len(items):
        waiting_States.extend(current_state.develop())
        waiting_States.sort(key=lambda x: x.upperbound)
        current_state = waiting_States.pop()
    best_solution = current_state
    best_item = []
    for i in range(len(best_solution.taken)):
        if (best_solution.taken[i] == 1):
            best_item.append(str(items[i]))
    return [best_item, best_solution.benefit]





