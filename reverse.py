def reverse(n):
    rev=0
    while(n>0):
        rem=n%10
        n=n//10
        rev=rev*10+rem
    return rev
    print(rev)
    '''
    a=len(n)
    for i in n[len(n),0,-1]:
        print(i)
    '''
