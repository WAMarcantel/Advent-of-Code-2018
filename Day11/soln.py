serial = int(open("input").readline())

grid = [[0 for i in range(300)] for j in range(300)]

for x in range(1,300):
    for y in range(1,300):
        rack_id = x + 10
        power_level = (rack_id * y) + serial
        power_level *= rack_id
        power_level = (int(power_level / 100) % 10) - 5

        grid[x-1][y-1] = power_level

max = -float('inf')
maxcoord = -1
for z in range(300):
    for i in range(300-z):
        for j in range(300-z):

            square = [item for sublist in list(map(lambda x: x[j:j+z], grid[i:i+z])) for item in sublist]
            s = sum(square)
            if s > max:
                max = s
                maxcoord = (i+1, j+1, z)


    print(max, maxcoord, z)

print(max, maxcoord)