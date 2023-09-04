def countdown(num):
    _list = []
    for x in range(num, 0, -1):
        _list.append(x)
    return _list

print(countdown(42))

def printAndReturn(x ,y):
    print(x)
    return y

print(printAndReturn(42, 4242))

list1 = [38, 422, "forty-two", 954]

def firstPlusLength(_list):
    return _list[0] + len(_list)

print(firstPlusLength(list1))

def valuesGreaterThanSecond(_list):
    temp = []
    for x in _list:
        if x > _list[1]:
            temp.append(x)
    if len(temp) >= 2:
        print(len(temp))
        return temp
    else:
        return "False"
    
print(valuesGreaterThanSecond([42,7,1,5,23,8]))
print(valuesGreaterThanSecond([42,7,1]))

def thisLengthThatValue(x,y):
    _list = []
    z = 0
    while(z < x):
        _list.append(y)
        z+=1
    return _list

print(thisLengthThatValue(4,7))
print(thisLengthThatValue(6,2))