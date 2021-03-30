# 数据结构与算法python实现
# 基本的数据结构
# 1、栈（LIFO）后进先出
# 栈的应用：每个 web 浏览器都有一个返回按钮。
# 当你浏览网页时，这些网页被放置在一个栈中（实际是网页的网址）。
# 你现在查看的网页在顶部，你第一个查看的网页在底部。如果按‘返回’按钮，将按相反的顺序浏览刚才的页面。
class Stack:
    # 初始化一个列表
    def __init__(self):
        self.items = []

    # 测试栈是否为空。不需要参数，并返回布尔值。
    def isEmpty(self):
        return self.items == []

    # 将一个新项添加到栈的顶部。它需要 item 做参数并不返回任何内容。
    def push(self,items):
        self.items.append(items)

    # 从栈中删除顶部项。它不需要参数并返回 item 。栈被修改。
    def pop(self):
        return self.items.pop()

    # 从栈返回顶部项，但不会删除它。不需要参数。 不修改栈。
    def peek(self):
        return self.items[len(self.items)-1]

    # 返回栈中的 item 数量。不需要参数，并返回一个整数。
    def size(self):
        return len(self.items)

# 2、队列（FIFO）先进先出
class Queue:
    # 初始化
    def __init__(self):
        self.items = []

    # 查看队列是否为空。它不需要参数，并返回布尔值。
    def isEmpty(self):
        return self.items == []

    # 从队首移除项。它不需要参数并返回 item。 队列被修改。
    def dequeue(self):
        return self.items.pop()

    # 将新项添加到队尾。 它需要 item 作为参数，并不返回任何内容。
    def enqueue(self, item):
        self.items.insert(0, item)

    # 返回队列中的项数。它不需要参数，并返回一个整数。
    def size(self):
        return len(self.items)

# 面试题：
# 1、如何实现用两个队列实现栈，并支持普通队列的全部四种操作
# 你只能使用队列的基本操作
# 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
# 你所使用的语言也许不支持队列。 
# 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
# 实现 MyStack 类：
    # void push(int x) 将元素 x 压入栈顶。
    # int pop() 移除并返回栈顶元素。
    # int top() 返回栈顶元素。
    # boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。


from collections import deque
class Stack_q:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    # 将元素 x 压入栈顶。
    def push(self, x):
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        return self.queue1.popleft()

    def top(self):
        return self.queue1[0]

    def empty(self):
        return not self.queue1

# 2、用栈实现队列
# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
#
# 实现 MyQueue 类：
    # void push(int x) 将元素 x 推到队列的末尾
    # int pop() 从队列的开头移除并返回元素
    # int peek() 返回队列开头的元素
    # boolean empty() 如果队列为空，返回 true ；否则，返回 false

class MyQueue:
    # 初始化
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]


    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def empty(self):
        return not self.stack1 and not self.stack2





