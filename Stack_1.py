from collections import deque

class myStack:
    
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self, x):
        # Push x first in empty q2
        self.q2.append(x)
        
        # Push all the remaining
        # elements in q1 to q2.
        while len(self.q1) != 0:
            self.q2.append(self.q1[0])
            self.q1.popleft()
        
        # swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1
        
    def pop(self):
        # if no elements are there in q1
        if len(self.q1) == 0:
            return
        self.q1.popleft()
        
    def top(self):
        if len(self.q1) == 0:
            return -1
        return self.q1[0]
        
    def size(self):
        return len(self.q1)

if __name__ == '__main__':
    st = myStack()
    st.push(1)
    st.push(2)
    st.push(3)
    
    print(st.top())
    st.pop()
    print(st.top())
    st.pop()
    print(st.top())
    
    print(st.size())
