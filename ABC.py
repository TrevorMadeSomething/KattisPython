# gameplan->
# take num, take order, make num a list and order it
# create a dictionary that attatches A -> low, C -> high
# make a new string by going through order and taking attatched value

num = input()
order = input()


def orderNumbers(num, order):
    answer = []
    tempAnswer = []

    num = num.split()
    for i in range(len(num)):
        num[i] = int(num[i])

    num.sort()

    dic = {'A': num[0], 'B': num[1], 'C': num[2]}

    for k in order:
        tempAnswer.append(dic.get(k))
    for value in tempAnswer:
        if value != None:
            answer.append(value)
    return answer


myAnswer = orderNumbers(num, order)
myAnswer = str(myAnswer).strip('[]')

print(myAnswer[0] + ' ' + myAnswer[3] + ' ' + myAnswer[6])
