def valid_parentheses(string):
    string = [c for c in string if c == "(" or c == ")"]
    if len(string) % 2 != 0:
        return False
    stack = []
    for c in string:
        if c == "(":
            stack.append(c)
        else:
            if not len(stack):
                return False
            else:
                d = stack.pop()
                if d != "(":
                    return False
    return not len(stack)
