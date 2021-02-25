names = input().split(", ")

heroes = {hero: {} for hero in names}
# dict with value new dict

command = input()
while command != "End":
    name, item, cost = command.split("-")
    if name in heroes:
        if item not in heroes[name]:
            heroes[name][item] = int(cost)

    command = input()

[print(f"{hero} -> Items: {len(heroes[hero])}, Cost: {sum(heroes[hero].values())}") for hero in heroes]