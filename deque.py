from collections import deque

def push_front(deq, item):
    deq.appendleft(item)
    print('ok')
    return deq

def push_back(deq, item):
    deq.append(item)
    print('ok')
    return deq

def pop_front(deq):
    if deq == deque():
        print('error')
    else:
        print(deq.popleft())
    return deq

def pop_back(deq):
    if deq == deque():
        print('error')
    else:
        print(deq.pop())
    return deq

def front(deq):
    if deq == deque():
        print('error')
    else:
        print(deq[0])
    return deq

def back(deq):
    if deq == deque():
        print('error')
    else:
        print(deq[-1])
    return deq

def size(deq):
    if deq == deque():
        print(0)
    else:
        print(len(deq))
    return deq

def clear(deq):
    deq.clear()
    print('ok')
    return deq

def exit_(deq):
    print('bye')
    return False


deq = deque()
funcs = [push_front, push_back, pop_front, pop_back, front, back, size, clear, exit_]
commands = ['push_front', 'push_back', 'pop_front', 'pop_back', 'front', 'back', 'size', 'clear', 'exit']
strg = ''
while strg != 'exit':
    strg = input()
    if strg in commands:
        funcs[commands.index(strg)](deq)
    else:
        a = list(strg.split())
        funcs[commands.index(a[0])](deq, int(a[1]))
        
