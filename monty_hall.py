import random

def monty_hall (reveal, switch):
    count = 10000000
    count_correct = 0
    for i in range(0, count):
        doors = [0, 0, 0]
        correct_answer = random.randint(0, 2)
        doors[correct_answer] += 1
        selection = random.randint(0, 2)
        revealed_door = -1
        if reveal:
            for i in range(2):
                if i != selection and i != correct_answer:
                    revealed_door = i

        if switch:
            for i in range(2):
                if i != selection and i != revealed_door:
                    selection = i

        if doors[selection] == 1:
            count_correct += 1

    return count_correct / float(count)


print('No Reveal: ' + str(monty_hall(False, False)))
print('Reveal, No Switch: ' + str(monty_hall(True, False)))
print('Reveal, Switch: ' + str(monty_hall(True, True)))
