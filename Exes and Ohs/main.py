def xo(s):
    s = s.lower()
    n_x = s.count('x')
    n_o = s.count('o')
    if n_o == n_x:
        return True
    else:
        return False
