def remove(s):
    if len(s)>0:
        if s[-1] == '!':
            return s[:-1]
        else:
            return s
    else:
        return s