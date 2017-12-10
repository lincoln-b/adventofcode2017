def parse(stream):
    group_count = 0
    group_scores = []
    in_garbage = False
    ignore = False
    for i in range(0,len(stream)):
        if ignore:
            ignore = False
        elif stream[i] == "!":
            ignore = True
        elif stream[i] == "<" and not in_garbage:
            in_garbage = True
        elif stream[i] == ">" and in_garbage:
            in_garbage = False
        elif stream[i] == "{" and not in_garbage:
            group_count += 1
        elif stream[i] == "}" and not in_garbage:
            group_scores.append(group_count)
            group_count -= 1
    return sum(group_scores)

# part 1
f = open("day9.data", "r")
# print parse(f.readline())

def remove(stream):
    group_count = 0
    group_scores = []
    in_garbage = False
    ignore = False
    garbage = 0
    for i in range(0,len(stream)):
        if ignore:
            ignore = False
        elif stream[i] == "!":
            ignore = True
        elif stream[i] == "<" and not in_garbage:
            in_garbage = True
        elif stream[i] == ">" and in_garbage:
            in_garbage = False
        elif stream[i] == "{" and not in_garbage:
            group_count += 1
        elif stream[i] == "}" and not in_garbage:
            group_scores.append(group_count)
            group_count -= 1
        elif in_garbage:
            garbage += 1
    return garbage

# part 2
print remove(f.readline())
