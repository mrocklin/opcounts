from sympy import *
n,m,k = symbols('n,m,k')

def test():
    file = open('opcounts.txt')
    lines = [line.strip()
                for line in file.readlines()
                if line.strip() and line[0]!='#']

    print "Errors found in the following lines:"
    print "===================================="
    for line in lines[1:]:
        adds, muls, flops = map(sympify, line.strip().split(',')[1:])
        residual = simplify(flops - (adds + muls))
        if residual == 0:
            continue
        #if residual.subs({n:2582, m:1827, k:285}) == 0:
        #    continue
        print line
        print "Residual: ", residual

if __name__ == "__main__":
    test()
