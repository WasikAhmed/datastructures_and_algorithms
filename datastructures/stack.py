class Stack:
    def __init__(self):
        self.stack = []
        self.Top = -1

    def is_empty(self):
        return self.Top == -1

    def push(self, element):
        self.Top += 1
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            self.Top -= 1
            return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def show(self):
        print(self.stack[::-1])


if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    print(stack.is_empty())
    print(stack.top())
    stack.show()
    print(stack.pop())
    print(stack.pop())
    stack.show()
