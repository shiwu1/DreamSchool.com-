source=input()
target=input()

#求解需要多少个source才能拼接成一个target
#法一：暴力。遍历目标字符串的同时遍历源字符串，这样可以保证相对顺序不变。
def func1(a,b):
    count=0
    i=0
    j=0
    while j<len(b):
        while i<len(a):
            
            if a[i]==b[j]:
                i=i+1
                j=j+1
            else:
                i=i+1
        #如果目标字符已经完成遍历但是元字符还未完成遍历，强制退出    
            if j==len(b):
                i=len(a)
        #如果源字符串已经遍历完毕但是目标字符串仍还有，则继续从头遍历源字符串
        #同时，源字符串需要的个数加一
        if i==len(a):
            i=0
            count=count+1
    return count

#判断target中是否有source中不存在的字符
for ch in target:
    if ch not in source:
        print(-1)
else:
    #求解需要多少个source才能拼接成一个target
    res=func1(source,target)
    print(res)