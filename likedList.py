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
        
        for i in range (index-1): #근데 이게 베스트 로직은 절대 아닐 것 같음 
            append_point = append_point.next
        temp_point = append_point.next
        append_point.next = node(data)
        append_point.next.next = temp_point
        self.count += 1
        return 
    
    def delete_index(self,index): #이게 구현이 노드를 리턴해주면 편한데, 그래도 일단 이렇게 했으니까 한번 해보자
        if(index < 0):
            print("인덱스는 0부터 시작입니다.")
            return 
        if(index > self.count):
            print("인덱스의 수가 링크 수 보다 큽니다")
            return
        if(index == 0):
            self.headNode = self.headNode.next
            self.count -=1
            return
        
        delete_point = self.headNode
        before_point = self.headNode
        for i in range (index):
            if (i != 0):
                before_point = before_point.next
            delete_point = delete_point.next
        temp_point = delete_point.next
        before_point.next = temp_point
        self.count -= 1
        return    
            
            
    def showAll(self):
        tail = self.headNode
        while(tail is not None):
            print(tail.data, end = " ")
            print("->",end=" ")
            tail = tail.next
        print()
   
        
