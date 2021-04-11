from collections import deque

materials = list(map(int, input().split()))
magic_values = deque(map(int, input().split()))

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy Bear",
    400: "Bicycle",
}

crafted = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy Bear": 0,
    "Bicycle": 0,
}

while materials and magic_values:
    current_box = materials.pop()
    current_magic = magic_values.popleft()
    total_magic = current_box * current_magic

    if total_magic in presents:
        crafted[presents[total_magic]] += 1
    else:
        if total_magic > 0:
            materials.append(current_box + 15)

        elif total_magic < 0:
            result = current_box + current_magic
            materials.append(result)

        else:
            if current_box:
                materials.append(current_box)
            if current_magic:
                magic_values.appendleft(current_magic)

success = crafted["Doll"] and crafted["Wooden train"] or crafted["Teddy Bear"] and crafted["Bicycle"]

if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {','.join(map(str, reversed(materials)))}")
if magic_values:
    print(f"Magic left: {', '.join(map(str, magic_values))}")

for key, value in sorted(crafted.items()):
    if value:
        print(f"{key}: {value}")



