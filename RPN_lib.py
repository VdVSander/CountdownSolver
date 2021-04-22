#Calculate the result of an operation
def calc(operand1, operand2, operator):
    if operator == '+':
        return operand1 +operand2
    elif operator == '-':
        return operand1-operand2
    elif operator == '*':
        return operand1*operand2
    elif operator == '/':
        return operand1/operand2
    else:
        print("ERROR: Operator not supported.")

#Decide what to do when a new item is added to the stack
def stackOperation(item, stack):
    operators = ['+','-','*','/']
    if item in operators and len(stack) >= 2:
        result = calc(stack.pop(0), stack.pop(0), item)
        stack = [result] + stack
        return stack
    elif item in operators and len(stack) < 2:
        print("ERROR: Wrong RPN.")
    else:
        stack = [item] + stack
        return stack

#Calculate the result of an operation in RPN
def calcRPN(RPN):
    stack = []
    for item in RPN:
        stack = stackOperation(item, stack)
        print(stack)
    return stack.pop(0)