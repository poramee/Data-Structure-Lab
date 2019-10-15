def knapsack(weight,availableList,inBagList):
    if weight == 0:
        print(">> ",inBagList)
        return 0
    elif weight < 0:
        return 0
    else:
        for i in range(0,len(availableList)):
            tempInBag = []
            tempInBag += inBagList
            tempInBag.append(availableList[i])
            knapsack(weight - availableList[i], availableList[(i+1):], tempInBag)

knapsack(20, [20, 10, 5, 5, 3, 2, 20, 10],[])
