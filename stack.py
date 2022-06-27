#stack 
#그래도 공부하는건데 파이썬 내부 메소드 사용 안하고 구현하기 
#로직은 맞는데, 빈 배열을 선언하고 할당하면 index out of range 에러가 뜸 -> 그래서 처음에 크기 입력 받기 

import math
from turtle import clear


class stack:
    def __init__(self):
        capacity = int(input("stack의 크기를 입력하세요"))
        self.stack = [0] * capacity
        self.count = 0 # 어차피 내가 공부하는건데, 내부 메소드 사용 안하려고 카운트 반환 
    
    def push(self,data):
        self.stack[self.count] = data
        self.count += 1 
        
    def pop(self): #스택이니까 후입 선출
        if(self.count == 0): #어차피 count로 관리하는거니까, isEmpty 메소드 필요 x
            print("this stack is empty")
            return
        popItem = self.stack[self.count - 1] # 인덱스 접근 -1 제발 숙지하기 
        print(popItem)
        self.stack[self.count -1 ] = 0 # 필수는 아닌데, 데이터 밀어버리기
        self.count -= 1 
        return popItem
    
    def showStack(self):
        if(self.count == 0): 
            print("this stack is empty")
            return
        for i in range(self.count):
            print(self.stack[i], end=' ')
        print()
            
    def showTop(self):
        if(self.count == 0): 
            print("this stack is empty")
            return
        print(self.stack[self.count])
        
tempstack = stack()

for i in range(5):
    tempstack.push(i * i)
    
tempstack.showStack()

data = tempstack.pop()

tempstack.showTop()


            