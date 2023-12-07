import string
drinks_costs = [[], [250, 0, 16, 1, -4], [350, 75, 20, 1, -7], [200, 100, 12, 1, -6]]
drinks = [400, 540, 120, 9, 550]
supply = ["water", "milk", "coffee", "cups"]
def remaining():
    print(f"The coffee machine has:\n{drinks[0]} ml of water\n{drinks[1]} ml of milk\n{drinks[2]} g of coffee beans\n{drinks[3]} disposable cups\n${drinks[4]} of money\n")

def buy():
    approved = 1
    type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    if type == 'back':
        pass
    else:
        for i in range(4):
            if drinks[i] < drinks_costs[int(type)][i]:
                print(f"Sorry, not enough {supply[i]}!")
                approved = 0
        if approved == 0:
            pass
        else:
            for i in range(5):
                drinks[i] -= drinks_costs[int(type)][i]

def fill():
    drinks[0] += int(input("Write how many ml of water you want to add: "))
    drinks[1] += int(input("Write how many ml of milk you want to add: "))
    drinks[2] += int(input("Write how many grams of coffee beans you want to add: "))
    drinks[3] += int(input("Write how many disposable cups you want to add: "))

def take():
    print(f"I gave you ${drinks[4]}\n")
    drinks[4] = 0

def exit():
    quit()

funcDict = {"remaining":remaining, "buy":buy, "fill":fill, "take":take, "exit":exit}
while True:
    action = input("Write action (buy, fill, take, remaining, exit):")
    funcDict[action]()