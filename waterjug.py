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

def water_jug_problem(capacity_a, capacity_b, target):
    jug_a = 0
    jug_b = 0

    while jug_a != target and jug_b != target:
        print(f"Jug A: {jug_a}L, Jug B: {jug_b}L")

        if jug_a == 0:
            jug_a = capacity_a
        elif jug_b == capacity_b:
            jug_b = 0
        else:
            pour_amount = min(jug_a, capacity_b - jug_b)
            jug_a -= pour_amount
            jug_b += pour_amount

    print(f"Jug A: {jug_a}L, Jug B: {jug_b}L")
    print("Target reached!")
capacity_a=int(input("enter the first jug water:"))
capacity_b=int(input("enter the second jug water:"))
target=int(input("enter the target water:"))
print(water_jug_problem(capacity_a,capacity_b,target))