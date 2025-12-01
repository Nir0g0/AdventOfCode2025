# Star 1

counterZero = 0
dial = 50

with open("input.txt") as file:
    for line in file:
        direction = line[:1]
        numberOfTurns = int(line[1:])

        if direction == 'L':
            dial = (dial - numberOfTurns) % 100
        else:
            dial = (dial + numberOfTurns) % 100

        if dial == 0: counterZero += 1

print(counterZero)


# Star 2

counterZero = 0
dial = 50

with open("input.txt") as file:
    for line in file:
        direction = line[:1]
        numberOfTurns = int(line[1:])
        
        for i in range(0, numberOfTurns, 1):
            if direction == 'L':
                dial = (dial - 1) % 100
            else:
                dial = (dial + 1) % 100
            
            if dial == 0: counterZero += 1

print(counterZero)