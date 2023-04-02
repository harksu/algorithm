n = int(input())
k = int(input())
#기본적인 입력값, 


def binary_search(target, start, end): #찾고자 하는 타겟의 이중 탐색
    while (start <= end):
        mid = (start + end) // 2

        count = 0
        for i in range(1, n+1):
             # 어차피 a배열은 i행이 모두 i의 배수이므로, 배열의 행의 수만큼 반복문을 돌려서 타겟보다 작은 수를 카운트 하면 된다.
            count += min(mid//i, n)
            print(i,count,mid,start)
             # 이때, 배열의 행의 수 보다 큰 값은 b 배열에는 들어갈 수 없으므로 n을 추가해서, 이 중 최소값을 카운트에 더한다.
        if count >= target:
            end = mid-1
        else:
            start = mid+1
    return start #타겟 인덱스의 값을 구하는 것이므로 결국 start를 반환하면 된다.


print(binary_search(k, 1, n*n))
