# https://www.reddit.com/r/dailyprogrammer/comments/7jkfu5/20171213_challenge_344_intermediate_bankers/

# Create a program that will read a text file with the banker’s algorithm in it, and output the order that the processes should go in. An example of a text file would be like this:
#
# [3 3 2]
#
# [0 1 0 7 5 3]
#
# [2 0 0 3 2 2]
#
# [3 0 2 9 0 2]
#
# [2 1 1 2 2 2]
#
# [0 0 2 4 3 3]
#
# And the program would print out:
#
# P1, P4, P3, P0, P2

input_file = '344-programs.txt'

processes = []
available = []

with open(input_file,'r') as f:
    available = list(map(int,(f.readline().strip('[]\n').split(' '))))
    for line in f:
        processes.append(list(map(int,(line.strip('[]\n').split(' ')))))

number_slots = len(available)
number_processes = len(processes)

finished = []
[finished.append(False) for i in range(number_processes)]

order = []

# print('avail', available)
# [print(proc) for proc in processes]
# print(finished)


def cycle(available, processes):
    for p_count, process in enumerate(processes):
        if p_count in order:
            continue
        for s_count, slot in enumerate(available):
            # print('P'+str(p_count), slot+process[s_count], process[s_count+number_slots])
            if slot+process[s_count] < process[s_count+number_slots]:
                break
            elif s_count+1 == number_slots:
                order.append(p_count)
                finished[p_count] = True
                for i in range(len(available)):
                    available[i] += process[i]
                return p_count

for i in range(number_processes):
    out = cycle(available, processes)
    # print('out', out, available)

# Formatting output
formatted = ''

for index in order:
    formatted = formatted + 'P'+str(index)+', '
print(formatted[:-2])