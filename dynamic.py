from item import Item
from settings import MAX_WEIGHT
maximum_weight = MAX_WEIGHT


class Pack:
    def __init__(self, items_given, max_weight=maximum_weight):
        self.max_weight = max_weight
        self.items_given = items_given
        self.stored_items = []
        self.s_matrix = [[0 for i in range(self.max_weight + 1)]
                         for j in range(len(self.items_given))]
        self.best_benefit = 0

    def fill_solver_matrix(self):
        for i in range(len(self.s_matrix)):
            for j in range(len(self.s_matrix[i])):
                if j < self.items_given[i].get_weight():
                    self.s_matrix[i][j] = self.s_matrix[i - 1][j]
                else:
                    self.s_matrix[i][j] = max(self.items_given[i].get_value() +
                                              self.s_matrix[i - 1]
                                              [j - self.items_given[i].
                                              get_weight()],
                                              self.s_matrix[i - 1][j])

    def get_stored_items(self):
        self.fill_solver_matrix()
        lead = (len(self.s_matrix) - 1,
                len(self.s_matrix[len(self.s_matrix) - 1]) - 1)
        self.best_benefit = self.s_matrix[lead[0]][lead[1]]
        while self.s_matrix[lead[0]][lead[1]] is not 0:
            if lead[0] == 0 or lead[1] == 0:
                self.stored_items.append(str(self.items_given[lead[0]]))
                break
            if self.s_matrix[lead[0]][lead[1]] == self.s_matrix[lead[0] - 1][lead[1]]:
                lead = (lead[0] - 1, lead[1])
            else:
                self.stored_items.append(str(self.items_given[lead[0]]))
                lead = (lead[0] - 1,
                        lead[1] - self.items_given[lead[0]].get_weight())
        return (self.stored_items, self.best_benefit)
