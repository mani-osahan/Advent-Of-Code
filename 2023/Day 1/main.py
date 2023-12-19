
def readFile(arr: list[str]):
    file_in = open('inputs.txt')
    lines = file_in.readlines()
    for i in lines:
        arr.append(i)
    return arr

def recoverInt(arr: list[str]):
    temp = []

    digits = { 
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    } 
 
  

    for i in arr:
        row = []
        if i in digits:
            print(i)
            temp.append(i)
        else:
            for j in i:
                if j.isnumeric():
                    row.append(j)
            temp.append(row)

    var_temp = []
    for i in temp: 
        if len(i) == 1:
            subOne = i[0] + i[0]
            var_temp.append(subOne)
        else:
            sub = i[0] + i[-1]
            var_temp.append(sub)

    total = list(map(int, var_temp))
    # print(total)
    total = sum(total)
    # print(total)

def main():
    arr = []
    readFile(arr)
    recoverInt(arr)

if __name__ == '__main__':
    main()
