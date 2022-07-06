A,B = map(int, input().split())
C = int(input())

carry = (B+C) / 60
minute = int((B+C) % 60)
hour = int((A + carry) % 24)

print(hour,minute)


#이거 좀 생각 잘한듯 ㅎㅎ