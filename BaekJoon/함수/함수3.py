def hansu(num) :
    hansu_cnt = 0 #처음 값은 0 
    for i in range(1, num+1): # 해당 수 까지 반복문을 돌리는데
        num_list = list(map(int,str(i)))
        if i < 100:
            hansu_cnt += 1  # 100보다 작으면 모두 한수(각 수의 차이가 동일하려면 100이 넘어야 됨)
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]: #이건 당연한거임 문제 잘 읽기.
            hansu_cnt += 1  # x의 각 자리가 등차수열이면 한수
    return hansu_cnt

num = int(input())
print(hansu(num))