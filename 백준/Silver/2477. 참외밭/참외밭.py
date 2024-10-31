K = int(input().strip())
lengths = []

for _ in range(6):
    direction, length = map(int, input().split())
    lengths.append(length)

max_width = max(lengths[0], lengths[2], lengths[4])
max_height = max(lengths[1], lengths[3], lengths[5])

total_area = max_width * max_height
small_width = lengths[(lengths.index(max_height) + 3) % 6]
small_height = lengths[(lengths.index(max_width) + 3) % 6]

empty_area = small_width * small_height
field_area = total_area - empty_area
result = field_area * K

print(result)
