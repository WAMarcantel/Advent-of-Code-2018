def read_input(file):
    input_file = open(file)

    l = []
    for line in input_file:

        if line[len(line) - 1] is "\n":
            line = (line[:len(line) - 1])

        l.append(line)

    return l[0].split()[2], l[2:]


raw_initial_state, raw_rules = read_input("input")

initial_state = set(i for i, c in enumerate(raw_initial_state) if c == "#")

rules = dict()
for rule in raw_rules:
    split_rule = rule.split()
    rules[split_rule[0]] = split_rule[2]


def next_generation(state, rules):
    min_index = min(state)
    max_index = max(state)

    new_state = set()
    for pot_index in range(min_index - 3, max_index + 4):
        pat = ''.join('#' if pot_index + pot_offset in state else '.' for pot_offset in [-2, -1, 0, 1, 2])
        if pat in rules:
            if rules[pat] == "#":
                new_state.add(pot_index)

    return new_state


current_state = initial_state
for i in range(20):
    current_state = next_generation(current_state, rules)

#p1 answer
print("p1 answer: ", sum(current_state))


# in this part, I experimented
sum_plants = 0
last_sum = 0
current_state = initial_state
for i in range(1, 102+1):

    current_state = next_generation(current_state, rules)
    sum_plants = sum(current_state)
    print('gens: ', i, 'sum: ', sum_plants, 'diff: ', sum_plants-last_sum)
    last_sum = sum_plants

print(sum_plants + (5e10 - 102) * 46)
# after 102 gens, the difference is the same
# so sum at 1000 == sum at 102 + 898 * 46