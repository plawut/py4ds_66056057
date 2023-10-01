

def calculateSum(list_data):
    total = 0
    if list_data.__len__() == 0:
        return 0
    else:
        for n in list_data:
            total += n
        return total


def calculateProdcut(list_data1):
    total1 = 1
    if list_data1.__len__() == 0:
        return 0
    else:
        for n in list_data1:
            total1 = total1*n
        return  total1


def calculateAVG(list_data2):
    total3 = 0
    if list_data2 == []:
        return []
    elif sum(list_data2) == 0:
        return 0
    else:
        for n in list_data2:
            total3 += n
        return  total3/ list_data2.__len__()


if __name__ == '__main__':
    # print(calculateSum([]) == 0)
    # print(calculateSum([2,4,6,8,10]) == 30)
    # print(calculateProdcut([]) == 0)
    # print(calculateProdcut([2,4,6,8,10]) == 3840)
    print(calculateAVG([1,2,3]) == 2)
    print(calculateAVG([1,2,3,1,2,3,1,2,3]) == 2)
    print(calculateAVG([12,20,37]) == 23)
    print(calculateAVG([0,0,0,0,0,0,0,]) == 0)
    print(calculateAVG([]) == [])
    print(medianCal([3,7,10,4,1,9,6,5,2,8]) == 55)

#%%
