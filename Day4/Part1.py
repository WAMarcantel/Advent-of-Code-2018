import datetime

def read_input(file):
    input_file = open(file)

    list = []
    for line in input_file:

        if line[len(line) - 1] is "\n":
            line = (line[:len(line) - 1])

        list.append(line)
    return list

def parse_event(last_id, event):
    eventparts = event.split()
    day = eventparts[0][1:len(eventparts[0])]
    time = eventparts[1][:len(eventparts[1])-1]
    hour = int(time[0:1])
    mins = int(time[3:len(time)])

    if eventparts[2] == "Guard":
        last_id = int(eventparts[3][1:len(eventparts[3])])
        sleeping = False
    elif eventparts[2] == "falls":
        sleeping = True
    else:
        sleeping = False

    return last_id, sleeping, day, hour, mins


events = read_input("Input")

days = dict()
last_id = None
for event in events:
    last_id, sleeping, day, hour, mins = parse_event(last_id, event)

    if day in days:
        if last_id not in days[day]:
            days[day][last_id] = [0] * 60
    else:
        days[day] = dict()
        days[day][last_id] = [0] * 60

    if hour != 0:
        continue

    if sleeping:
        days[day][last_id][mins] += 1
    else:
        days[day][last_id][mins] -= 1

# for day in days.keys():
#     for guard in days[day].keys():
#         print(days[day][guard])


guard_totals = dict()

for day in days.keys():
    for guard in days[day].keys():
        hasSlept = False
        running_sum = 0
        sum = 0
        for i in range(len(days[day][guard])):
            if days[day][guard][i] < 0:
                if hasSlept:
                    running_sum += days[day][guard][i]
            elif days[day][guard][i] > 0:
                hasSlept = True
                running_sum += days[day][guard][i]

            if running_sum > 0:
                days[day][guard][i] = 1
            else:
                days[day][guard][i] = 0

            sum += running_sum

        if guard in guard_totals:
            guard_totals[guard] += sum
        else:
            guard_totals[guard] = sum


# for day in days.keys():
#     for guard in days[day].keys():
#         print(days[day][guard])

maxguard = -1
max = -1
for guard in guard_totals.keys():
    print(guard_totals[guard])
    if guard_totals[guard] > max:
        maxguard = guard
        max = guard_totals[guard]

doubletime = -1
max = -1

for i in range(60):
    was_asleep = 0
    for day in days.keys():
        if maxguard in days[day]:
            was_asleep += days[day][maxguard][i]
    if was_asleep > max:
        max = was_asleep
        doubletime = i

print(maxguard)
print(doubletime)
print(maxguard * doubletime)