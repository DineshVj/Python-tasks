def calculator(x,y,op):
    if isinstance(x, int) and isinstance(y, int) and (op == '+' or op == '-' or op == '*' or op == '/'):
        if op == "+":
            return x+y
        elif op == "-":
            return x-y
        elif op == "*":
            return x*y
        else :
            return x/y
    else:
        return "unknown value"