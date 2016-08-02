import sys


def execute_code(code, limit=float('inf'), print_func=None, one_step=False, print2_func=None):
    if not print_func:
        def myPrint(x):
            print(x, end='')
        print_func = myPrint        

    if not print2_func:
        def myPrint(x):
            print(x, end='')
        print2_func = myPrint        

    mode = 0
    pat = ''
    sub = ''
    tex = ''
    
    while code:
        c, *code = code
        if mode == 0:
            if c == '/':
                mode += 1
            elif c == '\\':
                if code:
                    c, *code = code
                    print_func(c)
            else:
                print_func(c)

        elif mode == 1:
            if c == '/':
                mode += 1
            elif c == '\\':
                if code:
                    c, *code = code
                    pat += c
            else:
                pat += c

        elif mode == 2:
            if c == '/':
                mode += 1
            elif c == '\\':
                if code:
                    c, *code = code
                    sub += c
            else:
                sub += c

        elif mode == 3:
            tex += c

    
    if mode == 3:
        while pat in tex:
            if limit <= 0:
                output = "Substitution limit exceeded\n"
                output += "---------------------------\n"
                output += '/{}/{}/{}'.format(pat, sub, tex)
                print2_func(output)
                return

            idx = tex.index(pat)
            tex = list(tex)
            sub = list(sub)

            tex[idx:idx+len(pat)] = sub
            tex = ''.join(tex)
            sub = ''.join(sub)

            limit -= 1

        if tex and not one_step:
            execute_code(tex, limit, print_func, one_step)
        
        if one_step:
            print2_func(tex)


def main():
    if len(sys.argv) == 1:
        return

    code = ''
    with open(sys.argv[1]) as file:
        code = '\n'.join(line.rstrip('\n') for line in file)

    execute_code(code)

    

if __name__ == '__main__':
    main()
