from __future__ import print_function
from collections import deque
from io import StringIO
import sys
import tokenize

def get_input(*args, **kw):
    return input(*args, **kw)

class Stack(deque):
    push = deque.append
    def top(self):
        return self[-1]

class Machine:
    def __init__(self, code):
        self.data_stack = Stack()
        self.return_stack = Stack()
        self.instuction_pointer = 0
        self.code = code

    def pop(self):
        return self.data_stack.pop()

    def push(self, value):
        self.data_stack.push(value)

    def top(self):
        return self.data_stack.top()

    def run(self):
        while self.instuction_pointer < len(self.code):
            opcode = self.code[self.instuction_pointer]
            self.instuction_pointer += 1
            self.dispatch(opcode)
