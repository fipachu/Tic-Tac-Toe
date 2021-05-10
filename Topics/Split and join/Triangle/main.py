height = int(input())
for layer in range(height):
    base = 2 * height - 1
    width = 2 * layer + 1
    print(("#" * width).center(base))

# this makes the whole thing into a two-liner,
# while making it unreadable and horrible
# print("\n".join([("#" * (layer * 2 + 1)).center(height * 2 - 1) for layer in range(height)]))
