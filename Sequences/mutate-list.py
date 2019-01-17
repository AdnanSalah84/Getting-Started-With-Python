colors = ["red", "white", "blue"]

colors.append("orange")

colors.insert(1, "yellow")

colors.remove("blue")
print(colors)

last_color = colors.pop()

print(colors)

print(last_color)

colors.clear()

print(len(colors))