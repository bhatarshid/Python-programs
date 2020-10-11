operatorList = {      #this dict is for operator precedence
    '^' : 1,
    '/' : 2,
    '*' : 2,
    '-' : 3,
    '+' : 3
}

def pretopost(Q,operatorList):
    P = []
    Q.append(')')
    stk = ['(']
    for i in Q:
        if(i == '('):
            stk.append('(')
        elif i in operatorList:
            op = stk[-1]
            while(op in operatorList and operatorList[op]<=operatorList[i]):
                stk.remove(op) 
                P.append(op)
                op = stk[-1]
                    
            stk.append(i)
        elif(i == ')'):
            while(stk[-1] != '('):
                P.append(stk[-1])
                stk.remove(stk[-1])
            stk.pop(len(stk)-1)
        else:
            P.append(i)
    return P

Q = ['A','+','(','B','*','C','-','(','D','/','E','^','F',')','*','G',')','*','H']
P = pretopost(Q,operatorList)
