def valid_parentheses(string):
    counter = 0
    counter_2 = 0
    if len(string) > 0:
        my_list = list(string)
        for x in my_list:
            if x == '(':
                counter += 1
                counter_2 +=1
            if x == ')':
                counter -= 1
                counter_2 -=1
            if counter <0:
                return False
    if counter%2 == 1:
        return False
    if counter_2 > 0:
        return False
    return True
