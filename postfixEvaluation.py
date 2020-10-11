
def postfixEvaluation(operatorList,Q):
    #Q is expression stored in list in postfix form
    STACK = []
    TOP = -1
    for i in Q:
        if i in operatorList:
            A = STACK[TOP]
            STACK.remove(A)
            TOP = TOP - 1
            B = STACK[TOP]
            STACK.remove(B)
            TOP = TOP - 1
            if(i == '+'):
                STACK.append(B+A)
            elif(i == '-'):
                STACK.append(B-A)
            elif(i == '*'):
                STACK.append(B*A)
            elif(i == '/'):
                STACK.append(B/A)
            elif(i == '^'):
                STACK.append(B^A)
            TOP = TOP + 1
        else:
            STACK.append(int(i))
            TOP = TOP + 1
    return STACK[TOP]

operatorList = ['+','-','*','/','^']
print(postfixEvaluation(operatorList,['5','6','2','+','*','12','4','/','-']))