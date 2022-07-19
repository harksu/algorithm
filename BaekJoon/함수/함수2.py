
answers = []
for i in range(10000):
    answers.append(i+1)
removelist = []
def func(number,lists):
    result = number
    number1 = int(number%10)
    number2 = int((number%100)/10)
    number3 = int((number%1000)/100)
    number4 = int((number/1000))
    result = result + number1+number2+number3+number4
    if(number <= 10000 and result <= 10000):
        removelist.append(result)
    if(number>10000):
        return
    func(result,lists)
for i in range(10000):
    func(i+1,answers)
for i in set(removelist):
    answers.remove(i)
for i in answers:
    print(i)

