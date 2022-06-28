#likedlist

from mimetypes import init

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedLIst:
    def __init__(self):
        self.headNode = None
        self.count = 0
        
    def append(self, data):
        if(self.headNode == None):
            self.headNode = node(data)
            self.count += 1
            return 
        tail = self.headNode
        while(tail.next is not None):
            tail = tail.next
        tail.next = node(data)
        self.count += 1
        return
    
    def append_index(self,data,index):
        
        if(self.headNode == None):
            self.headNode = node(data)
            self.count += 1
            return
        if(index < 0):
            print("인덱스는 0부터 시작입니다.")
            return 
        if(index > self.count):
            print("인덱스의 수가 링크 수 보다 큽니다")
            return
        
        append_point = self.headNode #일단 초기 값은 무조건 시작점 , 와 링크드 리스트는 파이썬이 더 어려운 듯  
        
        if index == 0:
            temp_point = append_point
            self.headNode = node(data)
            self.headNode.next = temp_point
            self.count += 1
            return
        
        for i in range (index):
            append_point = append_point.next
        temp_point = append_point.next
        append_point.next = node(data)
        append_point.next.next = temp_point
        self.count += 1
        return 
        
    
    def showAll(self):
        tail = self.headNode
        while(tail is not None):
            print(tail.data, end = " ")
            print("->",end=" ")
            tail = tail.next
            
   
        
test = linkedLIst()
test.append(1)  
test.append(2)
test.append(3)
test.append(4)
test.append_index(5,0)


test.showAll() 
   