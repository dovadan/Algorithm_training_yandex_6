# -*- coding: utf-8 -*-
"""tr_6_3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12qeU_yBWpWtRla61eucLXK4IFbVNYYVy

A. Правильная скобочная последовательность
"""

lines=open('input.txt','r').readlines()
prts=list(lines[0].strip())


def isValid(prts):
    dt={')' : '(', ']' : '[', '}' : '{' }
    stack=[]
    for prt in prts:
        if prt not in dt: # встретили откр. скобку
            stack.append(prt)
        else: # встретили закр. скобку
            if not stack: # не осталось откр. скобок
                return 'no'
            if stack.pop() != dt[prt]:
                return 'no'
    if stack: # остались откр. скобки
         return 'no'
    return 'yes'

print(isValid(prts))

"""B. Великое Лайнландское переселение"""

lines=open('input.txt','r').readlines()
n=lines[0].strip()
a=list(map(int, lines[1].split()))

a=[(a[i],i) for i in range(len(a))]
stack=[]
ans=[-1]*len(a)

for city in a:
    if not stack: # реализуется только в начале
        stack.append(city)
    else:
        while stack and city[0] < stack[-1][0]:
            ans[stack[-1][1]] = city[1]
            stack.pop()
        stack.append(city)

print(*ans)

"""C. Минимум на отрезке"""

lines=open('input.txt','r').readlines()
n,k=list(map(int, lines[0].split()))
a=list(map(int, lines[1].split()))


def find_min_k(a,k):
    ans=[]
    deq=[]

    for i in range(k):
        if not deq:
            deq.append(a[i])
        else:
            while deq and a[i] < deq[-1]:
                deq.pop()
            deq.append(a[i])

    ans.append(deq[0])

    k-=1

    for i in range(k+1,len(a)):
        if a[i-k-1] == deq[0]:
            del deq[0]
        while deq and a[i] < deq[-1]:
            del deq[-1]
        deq.append(a[i])
        ans.append(deq[0])

    return ans

def find_min_k_slow(a,k):
    ans=[]
    for i in range(len(a)-k+1):
        ans.append(min(a[i:i+k]))
    return ans

find_min_k_slow(a,k)

import random

def test_functions():
    num_tests = 1000
    max_n = 100
    max_value = 10**9

    for _ in range(num_tests):
        n = random.randint(1, max_n)
        k = random.randint(1, n)

        a = [random.randint(-max_value, max_value) for _ in range(n)]


        result_slow = find_min_k_slow(a,k)
        result_fast = find_min_k(a,k)

        if result_slow != result_fast:
            print(f"find_min_slow: {result_slow}, find_min: {result_fast}")
            return False

    print("Все тесты пройдены успешно.")
    return True

test_functions()

lines=open('input.txt','r').readlines()
n,k=list(map(int, lines[0].split()))
a=list(map(int, lines[1].split()))

deq=[]

for i in range(k):
    if not deq:
        deq.append(a[i])
    else:
        while deq and a[i] < deq[-1]:
            deq.pop()
        deq.append(a[i])

print(deq[0])

k-=1

for i in range(k+1,len(a)):
    if a[i-k-1] == deq[0]:
        del deq[0]
    while deq and a[i] < deq[-1]:
        del deq[-1]
    deq.append(a[i])
    print(deq[0])

"""D. Постфиксная запись"""

lines=open('input.txt','r').readlines()
a=lines[0].split()

# prior={'+' : 1, '-' : 1, '*': 2}
st=set(['+','-','*'])
ans=0

stack=[]

for i in range(len(a)):
    if a[i] not in st:
        stack.append(a[i])
    else:
        if a[i]=='+':
            stack[-2]=int(stack[-2])+int(stack[-1])
            del stack[-1]
        elif a[i]=='*':
            stack[-2]=int(stack[-2])*int(stack[-1])
            del stack[-1]
        elif a[i]=='-':
            stack[-2]=int(stack[-2])-int(stack[-1])
            del stack[-1]
print(stack[0])

"""E. Значение арифметического выражения"""

def calc(a):
    st=set(['+','-','*'])
    ans=0

    stack=[]

    for i in range(len(a)):
        if a[i] not in st:
            stack.append(a[i])
        else:
            if a[i]=='+':
                stack[-2]=int(stack[-2])+int(stack[-1])
                del stack[-1]
            elif a[i]=='*':
                stack[-2]=int(stack[-2])*int(stack[-1])
                del stack[-1]
            elif a[i]=='-':
                stack[-2]=int(stack[-2])-int(stack[-1])
                del stack[-1]
    return(stack[0])

def proc(a):
    a=[a[i] for i in range(len(a)) if a[i] not in set(('\n'))]
    while a and a[0]==' ':
        del a[0]
    while a and a[-1]==' ':
        del a[-1]
    if not a:
        return 'wrong'


    count_prs=0
    l, r=-1, -10
    for i in range(len(a)):
        if a[i]=='(':
            l=i
            count_prs+=1
        if a[i]==')':
            r=i
            count_prs-=1
        if r==l+1:
            return False
    if count_prs != 0: return False

    b=[]
    num=[]
    symbs=set(['+','-','*','(',')'])
    for i in range(len(a)):
        if a[i].isdigit():
            num.append(a[i])
            if i == len(a)-1:
                b.append(''.join(num))
        elif a[i] in symbs or a[i] == ' ':
            if num:
                b.append(''.join(num))
                num=[]
            if a[i] != ' ':
                b.append(a[i])
        else:
            return False

    l, r=-1, -10
    for i in range(len(b)):
        if b[i]=='(':
            l=i
        if b[i]==')':
            r=i
        if l==r+1:
            return False

    count=0
    for i in range(len(b)):
        if b[i].isdigit():
            count+=1
        else:
            count=0
        if count>1:
            return False

    count=0
    prior={'+' : 1, '-' : 1, '*': 2}
    for i in range(len(b)):
        if b[i] in prior:
            count+=1
        else:
            count=0
        if count>1:
            return False

    c=[]
    if b[0]=='-':
        c.append('0')
    for i in range(len(b)):
        if b[i] == '(':
            if b[i+1] == '-':
                c.append(b[i])
                c.append('0')
            else:
                c.append(b[i])
        else:
            c.append(b[i])

    return c



lines=open('input.txt','r').readlines()
a=lines[0]

def sol(a):

    c=proc(a)
    if c == False:
        return 'WRONG'

    try:
        prior={'+' : 1, '-' : 1, '*': 2}
        stack=[]
        ans=[]

        for token in c:
                if token.isdigit():
                    ans.append(token)
                elif token in prior:
                    while stack and stack[-1] in prior and prior[stack[-1]] >= prior[token]:
                        ans.append(stack.pop())
                    stack.append(token)
                elif token == '(':
                    stack.append(token)
                elif token == ')':
                    while stack and stack[-1] != '(':
                        ans.append(stack.pop())
                    if stack and stack[-1] == '(':
                        stack.pop()
        while stack:
            ans.append(stack.pop())

        return calc(ans)

    except:
        return 'WRONG'

print(sol(a))

"""F. Минимальная ПСП"""

lines=open('input.txt','r').readlines()
n=int(lines[0].strip())
order=list(lines[1].strip())
s=list(lines[2].strip())

close_open={')' : '(', ']' : '['}
open_close={'(' : ')', '[' : ']'}

stack=[]
for i in range(len(s)):
    if s[i] not in close_open:
        stack.append(s[i])
    else:
        stack.pop() # в стеке остаются только открытые скобки

rem=n-len(s) # осталось пустых мест
open_par=len(stack)
# если можем закрыть все скобки в стеке, то делаем выбор
# иначе просто закрываем последнюю скобку подходящей

def choose(open_bracket): # [ (
    ignore=list(close_open.keys())
    for i in range(2):
        if ignore[i] == open_close[open_bracket]:
            del ignore[i]
            break
    for i in range(4):
        if order[i]!=ignore[0]:
            return order[i]
res=s.copy()
while rem!=0:
    if rem-len(stack)>0:
        if not stack:
            for i in range(4):
                if order[i] in open_close:
                    stack.append(order[i])
                    res.append(order[i])
                    rem-=1
                    break
        else:
            par=choose(stack[-1])
            if par in close_open:
                res.append(par)
                del stack[-1]
                rem-=1
            else:
                res.append(par)
                stack.append(par)
                rem-=1
    else:
        par=open_close[stack[-1]]
        rem-=1
        res.append(par)
        del stack[-1]

for i in range(len(res)):
    print(res[i],end='')

"""G. Очередь в ПВЗ"""

lines=open('input.txt','r').readlines()
n,b=list(map(int, lines[0].split()))
a=list(map(int, lines[1].split()))

def find_time(n,b,a):
    total_time=0
    q=[]
    n=len(a)
    for i in range(n):
        q.append(a[i])
        rem=b
        obs=0
        # print(i+1,'минута')
        while q and rem>0:
            obs=min(rem,q[0])
            total_time+=obs*len(q)
            # print('добавили',obs*len(q))
            # print('до обслуживания',q)
            q[0]=max(0,q[0]-rem)
            # print('после обслуживания',q)
            if q[0]==0:
                del q[0]
                # print('удалили нулевой элемент',q)
            rem=rem-obs
    # print('осталось',q)
    # print('без неуспевших',total_time)
    while q:
        total_time+=q[0]*(len(q)+1)
        # print('прибавили',q[0]*(len(q)+1))
        del q[0]

    return total_time

print(find_time(n,b,a))

"""H. Стек с суммой"""

class stack_sum():
    def __init__(self):
        self.stack=[]
        self.prefix=[0]

    def add(self, x):
        self.stack.append(x)
        self.prefix.append(self.prefix[-1]+x)

    def spop(self):
        deleted = self.stack[-1]
        del self.stack[-1]
        del self.prefix[-1]
        return deleted

    def get_sum(self,k):
        return self.prefix[-1]-self.prefix[len(self.prefix)-k-1]


lines=open('input.txt','r').readlines()
n=int(lines[0].strip())

s=stack_sum()

for i in range(1,n+1):
    if lines[i].strip()[0]=='+':
        x=int(''.join(lines[i].strip()[1:]))
        s.add(x)
        # print('добавили',x)
        # print('теперь стек', s.stack)

    elif lines[i].strip()[0]=='?':
        k=int(''.join(lines[i].strip()[1:]))
        print(s.get_sum(k))
        # print('сейчас стек', s.stack)

    elif lines[i].strip()[0]=='-':
        print(s.spop())
        # print('удалили',x)
        # print('сейчас стек', s.stack)

"""I. Автоматизированный склад"""

lines=open('input.txt','r').readlines()
n=int(lines[0].strip())
a,b=list(map(int, lines[1].split()))


# test=[line.strip() for line in lines] # убрать после тестов
# test=[ln for ln in test if ln]
# n=len(test)-2
if a>b:
    a,b=b,a

priority={ (1,2) : (1, 2, 3, 4),
       (2,3): (2, 3, 4, 1),
       (3,4): (3, 4, 1, 2),
       (1,4): (4, 1, 2, 3),
       (1,3) : (1, 3, 2, 4),
       (2,4) : (2, 4, 1, 3),
}

straight=set([ (1,3),(3,1),(2,4),(4,2) ])

rules=priority[(a,b)]

matr=[[None,None,None,None] for i in range(450)]
for i in range(n):
    d,t=list(map(int, lines[i+2].split()))
    matr[t-1][d-1]=i+1

sides=[[],[],[],[]]
cur_time=0

ans=[0]*n

if (a,b) not in straight:
    for i in range(len(matr)):
        cur_time+=1
        for j in range(4):
            if matr[i][j] != None:
                sides[j].append(matr[i][j])
        # print('до', sides)
        find=False
        for j in rules:
            j-=1
            if find:
                break
            if sides[j]:
                number=sides[j][0]
                ans[number-1]=cur_time
                find=True
                del sides[j][0]
                break
        # print('после', sides)
else:
    for i in range(len(matr)):
        cur_time+=1
        for j in range(4):
            if matr[i][j] != None:
                sides[j].append(matr[i][j])
        # print('до', sides)
        find=False
        for j in rules[0:2]:
            j-=1
            if sides[j]:
                number=sides[j][0]
                ans[number-1]=cur_time
                find=True
                del sides[j][0]
        if find:
            # print('после', sides)
            continue
        for j in rules[2:4]:
            j-=1
            if sides[j]:
                number=sides[j][0]
                ans[number-1]=cur_time
                find=True
                del sides[j][0]
        # print('после', sides)

for i in range(len(ans)):
    print(ans[i])

"""J. Кровать из стульев"""

lines=open('input.txt','r').readlines()
n,H=list(map(int, lines[0].split()))
h=list(map(int, lines[1].split()))
w=list(map(int, lines[2].split()))


def find_min(h,w,H):

    n=len(h)
    chairs=[ (i+1,h[i],w[i]) for i in range(n) ] # (номер, h, w)
    chairs=sorted(chairs,key=lambda x: x[1])
    print(chairs)

    res=[]
    sum=0
    modules=[]
    r=0
    for l in range(n):
        if l==r:
            modules=[0]
            print('указатели совпадают. сейчас:',modules)
            sum=chairs[r][2]
        while r<n-1 and sum<H:
            r+=1
            sum+=chairs[r][2]
            abst=chairs[r][1]-chairs[r-1][1] # всегда >= 0
            print('текущая разность:',abst)
            # if modules[0]==abst:
            #     del modules[0]
            while modules and abst>modules[-1]:
                print('попался элемент > текущего. до:', modules)
                del modules[-1]
                print('попался элемент > текущего. после:', modules)
            print('идем вправо. до:', modules)
            modules.append(abst)
            print('идем вправо. после:', modules)
        if sum>=H:
            res.append(modules[0])
        print('окно:',l,r)
        sum-=chairs[l][2]
        if l+1<=n-1 and abs(chairs[l][1]-chairs[l+1][1])==modules[0]:
            print('двигаем левую границу. 0й эл. modules. до: ', modules)
            del modules[0]
            print('двигаем левую границу. 0й эл. modules. после: ',modules)

    print(res)
    return min(res)


print(find_min(h,w,H))

lines=open('input.txt','r').readlines()
n,H=list(map(int, lines[0].split()))
h=list(map(int, lines[1].split()))
w=list(map(int, lines[2].split()))


def find_min(h,w,H):

    n=len(h)
    chairs=[ (i+1,h[i],w[i]) for i in range(n) ] # (номер, h, w)
    chairs=sorted(chairs,key=lambda x: x[1])

    # h=[chairs[i][1] for i in range(len(chairs))]
    # w=[chairs[i][2] for i in range(len(chairs))]
    # print('h',h)
    # print('w',w)

    res=[]
    sm=0
    modules=[]
    r=0
    for l in range(n):
        if l==r:
            modules=[0]
            sm=chairs[r][2]
        while r<n-1 and sm<H:
            r+=1
            sm+=chairs[r][2]
            abst=chairs[r][1]-chairs[r-1][1] # всегда >= 0
            # if modules[0]==abst:
            #     del modules[0]
            while modules and abst>modules[-1]:
                del modules[-1]
            modules.append(abst)
        if sm>=H:
            res.append(modules[0])
        sm-=chairs[l][2]
        if l+1<=n-1 and abs(chairs[l][1]-chairs[l+1][1])==modules[0]:
            del modules[0]

    # print('res',res)
    return min(res)


print(find_min(h,w,H))