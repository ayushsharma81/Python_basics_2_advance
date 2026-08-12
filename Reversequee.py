from collections import deque

def reverseQueue(q):
    st = []
    
    # Transfer all elements from queue to stack
    while q:
        st.append(q[0])
        q.popleft()
    
    # Transfer all elements back from stack to queue
    # This reverses the order
    while st:
        q.append(st.pop())

if __name__ == "__main__":
    q = deque([5, 10, 15, 20, 25])
    
    reverseQueue(q)
    
    while q:
        print(q.popleft(), end=' ')
