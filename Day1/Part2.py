def update_frequency(delta):
    sign = 1
    if delta[0] is "-":
        sign = -1

    return sign * int(delta[1:len(delta)])

freq = 0
input_file = open("./Part1Input")

freqMap = dict()
list = []

for line in input_file:
    if line[len(line)-1] is "\n":
        list.append(line[:len(line)-1])
    else:
        list.append(line)


print(list)
i = 0
while True:
    freq += update_frequency(list[i%len(list)])
    if freq in freqMap:
        print(freq)
        break
    else:
        freqMap[freq] = True
        i += 1
