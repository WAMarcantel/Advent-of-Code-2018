def read_input(file):
    input_file = open(file)

    list = []
    for line in input_file:

        if line[len(line) - 1] is "\n":
            line = (line[:len(line) - 1])

        list.append(line)
    return list

def checksum(identifier):

    m = dict()
    is_two = False
    is_three = False

    for char in identifier:
        if char in m:
            m[char] += 1
        else:
            m[char] = 1

    for key in m.keys():
        if m[key] == 2:
            is_two = True
        if m[key] == 3:
            is_three = True

    return is_two, is_three


def editDistance(str1, str2):
    distance = 0
    for i in range(min(len(str1), len(str2))):
        if str1[i] is not str2[i]:
            distance += 1

    return distance


list = read_input("./Part1Input")

# twos = 0
# threes = 0
# for item in list:
#     isTwo, isThree = checksum(item)
#     twos += int(isTwo)
#     threes += int(isThree)
#
# print(twos*threes)

sameLetters = ""
breaking = False
for identifier in list:

    for otherIdentifier in list:

        if editDistance(identifier, otherIdentifier) == 1:

            for i in range(len(identifier)):
                if identifier[i] is otherIdentifier[i]:
                    sameLetters += identifier[i]

            breaking = True

        if breaking:
            break

    if breaking:
        break

print(sameLetters)
