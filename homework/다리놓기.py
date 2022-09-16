#조합 공식 mCn -> (m!)/{(m-n)!n!}
import math
t = int(input())#test case

for i in range(t):
    left,right = map(int, input().split())
    result = math.factorial(right)//(math.factorial(left)*math.factorial(right-left)) 
    print(result)