import sys


def update_frequency(delta):
    sign = 1
    if delta[0] is "-":
        sign = -1

    return sign * int(delta[1:len(delta)])



freq = 0
input_file = open("./Part1Input")

while True:
    freq += update_frequency(input_file.readline())
    print(freq)
