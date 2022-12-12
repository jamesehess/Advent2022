# -----------------------
#   Advent of Code 2022
#   Day 11 Part 1
#   Author: James Hess
# -----------------------


#Monkey 0:
#  Starting items: 79, 98
#  Operation: new = old * 19
#  Test: divisible by 23
#    If true: throw to monkey 2
#    If false: throw to monkey 3

inputs = []
inspects = []

with open("Day11Input.txt") as file:
    for input_monkey in file.read().split("\n\n"):
        temp = input_monkey.split("\n")
        temp_stripped = []
        for item in temp:
            temp_stripped.append(item.strip())
        inputs.append(temp_stripped)

class monkey:
    monkeys = []
    def __init__(self, number, items=[], operation=[], test=0, test_true=0, test_false=0):
        self.number = number
        self.items = items
        self.operation = operation
        self.test = test
        self.test_true = test_true
        self.test_false = test_false
        self.inspects = 0
        self.__class__.monkeys.append(self)

    def get_monkey(self, number):
        for monkey in self.monkeys:
            if monkey.number == number:
                return monkey

    def add_item(self, item):
        self.items.append(item)

    def throw_item(self, monkey):
        monkey.items.append(self.items[0])
        self.items.remove(self.items[0])

    def operate(self):
        self.inspects +=1
        if self.operation[1] == "old":
            value = self.items[0]
        else:
            value = int(self.operation[1])
        if self.operation[0] == "*":
            self.items[0] = int((self.items[0] * value)/3)
        elif self.operation[0] == "+":
            self.items[0] = int((self.items[0] + value)/3)

    def test_item(self):
        if self.items[0] % self.test == 0:
            self.throw_item(self.get_monkey(self.test_true))
        else:
            self.throw_item(self.get_monkey(self.test_false))

# initialize monkeys
for monk in inputs:
    monkey_number = int(monk[0].split()[1].replace(":",""))
    monkey_items = []
    for item in monk[1].replace("Starting items: ", "").split(", "):
        monkey_items.append(int(item))
    monkey_operation = monk[2].replace("Operation: new = old ", "").split()
    monkey_test = int(monk[3].replace("Test: divisible by ", ""))
    monkey_test_true = int(monk[4].replace("If true: throw to monkey ", ""))
    monkey_test_false = int(monk[5].replace("If false: throw to monkey ", ""))
    test_monkey = monkey(monkey_number, monkey_items, monkey_operation, monkey_test, monkey_test_true, monkey_test_false)

for round in range(20):
    for monkey in test_monkey.monkeys:
        for item in range(0,len(monkey.items)):
            monkey.operate()
            monkey.test_item()

for m in test_monkey.monkeys:
    inspects.append(m.inspects)
inspects.sort(reverse=True)
print(inspects[0]*inspects[1])