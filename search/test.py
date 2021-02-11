
BooleanFoodState = [False, False, False]
foodGrid = [(5, 5), (2, 2), (0, 0)]
position = (0, 5)
distance_between_foods = 0


def ManDistance(x, y):
    a1, b1 = x
    a2, b2 = y
    return abs(a1-a2) + abs(b1-b2)


for i, firstFood in enumerate(foodGrid):
    if BooleanFoodState[i]:
        continue
    for j, secondFood in enumerate(foodGrid[i+1:]):
        print(i+1)
        if BooleanFoodState[i+1]:
            continue
        distance = ManDistance(firstFood, secondFood)
        if distance > distance_between_foods:

            distance_between_foods = distance
            distance_to_pacman = min(ManDistance(
                firstFood, position), ManDistance(secondFood, position))
            heuristic = distance_between_foods + distance_to_pacman
print(heuristic)


def findFurthestPoints(aList):
    if len(aList) == 1:
        return aList[0]
    elif len(aList) == 0:
        return 0

    max_distance = 0
    for i, first in enumerate(aList):
        print(first)
        for second in aList[i+1:]:
            distance = ManDistance(first, second)
            if distance > max_distance:
                firstNode = first
                secondNode = second
                max_distance = distance
    return firstNode, secondNode, max_distance


a, b, c = findFurthestPoints([(0, 0), (5, 5), (3, 3), (6, 7)])
print(a, b, c)
