
from ShuntingYard import *

shunt = ShuntingYard()

if __name__ == '__main__':
    infix = '( 5 * ( -4 * ( 3 * ( 2 * ( 1 * 9 ) / 8 - 7 ) + 6 ) ) )'
    print( 'For infix expression: %r\n' % infix )
    rp = shunt.doShuntingYard(shunt.tokenizeInput(infix))
    # maxcolwidths = [len(max(x, key=len)) for x in zip(*rp)]
    # row = rp[0]
    # print( ' '.join('{cell:^{width}}'.format(width=width, cell=cell) for (width, cell) in zip(maxcolwidths, row)))
    # for row in rp[1:]:
        # print( ' '.join('{cell:<{width}}'.format(width=width, cell=cell) for (width, cell) in zip(maxcolwidths, row)))
 
    #print('\n The final output RPN is: %r' % rp[-1][2])
    print(*rp)