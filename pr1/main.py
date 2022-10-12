from gui import *

priority = {
    '(': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}

brackets = {
    '(': ')',
    '[': ']',
    '{': '}'
}


class Calculator:
    def __init__(self):
        self.gui = Gui(self)
        self.values = None

    def convert(self, infix_string):
        infix_string = '(' + infix_string + ')'
        postfix = ''
        stack = []
        buf = ''
        for i in infix_string:
            if i.isalpha():
                buf += i
            elif len(buf) > 0:
                postfix += buf + ' '
                buf = ''
            if i in priority.keys() and i not in brackets.keys():
                while stack and priority[i] <= priority[stack[-1]]:
                    postfix += stack.pop() + ' '
                stack.append(i)
            elif i in brackets.keys():
                stack.append(i)
            elif i in brackets.values():
                while stack and stack[-1] not in brackets.keys():
                    postfix += stack.pop() + ' '
                if stack:
                    del stack[-1]

        self.postfix = postfix

    def calculate(self):
        buf = ''
        stack = []
        for i in self.postfix:
            if i.isalpha():
                buf += i
            elif len(buf) > 0:
                stack.append(self.values.get(buf))
                buf = ''
            if i in priority.keys() and i not in brackets.keys():
                if len(stack) > 1:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(self.calc(b, a, i))
        self.result = stack.pop()

    def calc(self, a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a / b
        elif operator == '^':
            return a ** b


if __name__ == '__main__':
    calculator = Calculator()
    calculator.gui.start()

'''
a + b * c * d + (e - f) * (g * h + i)
'''
