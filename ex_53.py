large, medium, small = [], [], []

def check_right_syntax(list_for_check):
    if list_for_check.count('(') != list_for_check.count(')'):
        return False

    syntax = []

    for i in list_for_check:
        if i == '(':
            syntax.append(i)
        if i == ')':
            if len(syntax) == 0:
                return False
            
            syntax.pop()
    
    return True


data = list(input().split())

print(check_right_syntax(data))