#Stacks: LIFO
'''Append: Push an  item on the stack
Pop: Remove an item from the stack. '''

#Stack Push
my_stack =[]
my_stack.append(3)
my_stack.append(2)
my_stack.append(5)
my_stack.append(8)
my_stack.append(11)
print(my_stack)


#Stack Pop
my_stack.pop()
print("After Popping last element: " ,my_stack)

class Stack():
    def __init__(self) -> None:
        self.stack = list()
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if(len(self.stack) >0):
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if(len(self.stack) >0):
            return self.stack[len(self.stack)-1]
        else:
            return None
    def __str__(self) -> str:
        return str(self.stack)

MY_Stack = Stack()
MY_Stack.push(1)
MY_Stack.push(2)
MY_Stack.push(3)
print(MY_Stack)
print(MY_Stack.peek())
print(MY_Stack.pop())
