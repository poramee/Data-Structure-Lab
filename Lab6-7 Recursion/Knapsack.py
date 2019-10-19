def knapsack(weight,availableList,inBagList):
    if weight == 0:
        print(inBagList)
        return
    if weight < 0 or len(availableList) == 0:
        return

    temp = []
    temp += inBagList
    temp.append(availableList[0])

    knapsack(weight - availableList[0],availableList[1:],temp)
    knapsack(weight,availableList[1:],inBagList)

knapsack(20, [20, 10, 5, 5, 3, 2, 20, 10],[])
