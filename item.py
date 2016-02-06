class Item:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight
        self.efficiency = value / weight

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_efficiency(self):
        return self.efficiency

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight
