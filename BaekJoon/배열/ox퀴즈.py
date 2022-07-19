t = int(input())
for i in range(t):
    sum = 0
    score =0
    answer = input()
    lists = list(answer)
    for i in lists:
        if i == 'O':
            score += 1
            sum = sum + score
        else:
            score = 0       
    
    print(sum)
                