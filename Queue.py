from queue import Queue
q = Queue(maxsize=3)
print("Initial size:", q.qsize())

q.put('a')
q.put('b')
q.put('c')
print("Is full:", q.full())

print("Elements dequeued from the queue:")
print(q.get())
print(q.get())
print(q.get())
print("Is empty:", q.empty())

q.put(1)
print("Is empty:", q.empty())
print("Is full:", q.full())
