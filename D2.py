import sys

for line in sys.stdin:
    a = line.strip()
    print(a)
    
    #创建一个空栈。遍历字符串中的每个字符。
    #如果字符是左括号（例如 '('、'{'、'['），则将其压入栈中。
    #如果字符是右括号，则检查栈是否为空：
    #如果栈为空，说明没有对应的左括号，在该右括号下标处标记问号。
    #如果栈不为空，弹出栈顶元素，检查弹出的左括号与当前右括号是否匹配：
    #如果匹配，继续遍历下一个字符。
    #如果不匹配,在当前右括号下标处标记问号,并将栈中剩余的左括号对应的下标处标记x。
    
    stack=[]
    l=['(',')','[',']','{','}']
    mapping={')':'(',']':'[','}':'{'}
    #结果先全部初始化为用空格占位，再根据左右括号的情况放置对应的字符
    res=[' ']*len(a)
    dic={}
    for i in range(len(a)):
        ch=a[i]
        #只有括号需要处理和判断，其余的字符直接跳过即可
        if ch in l:       
            if ch in mapping:
                if not stack or stack[-1][0]!=mapping[ch]:
                    res[i]='?'
                else:
                    stack.pop()
            else:
                #将左括号和对应的下标都押入栈中，方便后续对只有左括号的情况处理
                stack.append((ch,i))                  
    while stack:
        ch,index=stack.pop()
        res[index]='x'
        
    res=''.join(res)
    print(res)