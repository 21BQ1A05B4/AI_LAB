'''
                    WATER JUG PROBLEM
                    ------------------
            
description :   we have to maintain 2 litres of water in the 4 litre 
                which have no markings on the jars with the help of 3 litre jug

1. Consider two jugs one is capable of storing 4 litre and other of 3 litre
    (x, y) --> (4 litre, 3 litre)
2. Initially both are empty i.e.,
    (0, 0) --> (empty, empty)
3. fill the 3 litres jug completely
    (0, 3) --> (empty, 3)
4. next pour the water from the 3 litre jug to 4 litre jug 
    (3, 0) --> (3, empty)
5. again fill the 3 litre jug with water completely
    (3, 3) --> (3, 3)
6. then after fill the remaining part in the 4 litre jug i.e.,
    (4, 2) --> (4 litre, 2, litre)
7. empty the 4 four litre jug i.e.,
    (0, 2) --> (empty, 2)
8. fill the 4 litre jug with 2 litre present in the 3 litre jug
    (2, 0) --> (2 litre, empty)
9. therefore the final outcome is completed it means we have 
    filled the 4 litre jug equal to 2 litre

'''

visited = []
found = False


def findGoal(state, operations, output):
    global visited
    global found

    x1, y1 = state
    ops = [
        [x, y1],
        [x1, y],
        [0, y1],
        [x1, 0],
        [0, x1 + y1] if y-(x1+y1) >= 0 else [x1 + y1 - y, y],
        [x1 + y1, 0] if x-(x1+y1) >= 0 else [x, x1 + y1 - x]
    ]
    if goal in ops:
        found = True
        operations.append(ops.index(goal))
        output.append(goal)
        print("\n\nThe sequence of operations is:",operations, "\nThe sequence is:\n", output)
    else:
        for op in ops:
            if op not in visited:
                visited.append(op)
                l = operations + [ops.index(op)]
                out = output + [op]
                findGoal(op, l, out)


if __name__ == "__main__":
    x, y = map(int, input("Enter the capacities: ").split())
    goal = list(map(int, input("Enter the goal capacities: ").split()))
    initialstate = [0, 0]
    operations = []
    output = []

    visited.append(initialstate)
    findGoal(initialstate, operations, output)

    if not found:
        print("Not possible!")