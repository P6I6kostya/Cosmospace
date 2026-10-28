#Файл со всеми списками специальностей в одном Вузе
f = open('СПбГУ2.txt',encoding = 'utf-8')
#Количество олимпиадников скорее всего подающих в этот вуз: A01+A00/2
#Количество бюджетных мест в вузе по специальностям
k1,k2,k3,k4,k5,k6,k7,k8,k9 = 51,18,48,137,40,40,40,37,16 #СПбГУ
#k1,k2,k3,k4,k5,k6,k7,k8,k9 = 74,32,50,73,70,0,0,0,0 #ЛЭТИ
#k1,k2,k3,k4,k5,k6,k7,k8,k9 = 27,43,41,28,41,0,0,0,0 #КНИТУ
#k1,k2,k3,k4,k5,k6,k7,k8,k9 = 75,24,59,45,60,24,21,0,0 #ГУАП
#k1,k2,k3,k4,k5,k6,k7,k8,k9 = 25,26,76,42,90,0,0,0,0 #СПбГУТ
mk = [0,k1,k2,k3,k4,k5,k6,k7,k8,k9]
# ВСЕ ЗАЯВКИ
A = []
k = 0
for s in f:
    n = []
    l = ''
    if s[0] not in '0123456789':
        k = k+1
    else:
        for x in range(0,len(s)):
            if s[x]==' ' or s[x] in '\t':
                if len(l)>0:
                    if l[0] in '1234567890':
                        l = int(l)
                    n.append(l)
                    l = ''
            else:
                l = l+s[x]
        A.append([k,n])
### КОЛИЧЕСТВО УЧАСТНИКОВ
A20 = set()
for z1 in A:
    k,x1 = z1
    for y1 in x1:
        if isinstance(y1,int):
            if y1>100000 and y1<10000000:
                A20.add(y1)
A2 = []
for x in A20:
    A2.append(x)
A2 = sorted(A2)
A11 = []
A00 = []
A01 = []
A33 = []
# КОЛИЧЕСТВО ЗАЯВОК1(без шлака),ОЛИМПИАДНИКОВ и ЗАЯВОК 
for z1 in A:
    k,x = z1
    if len(x)<=12:
        continue
    else:
        A11.append(z1)
    if isinstance(x[4],str):
        if len(x[2])>5:
            A01.append(z1)
        else:
            A00.append(z1)
    if len(x[2])>5:
        A33.append(z1)
print("Олимпиадники с согласием", "/ без согласия")
print(len(A01),len(A00))
ko = len(A01)+len(A00)//2
sk = sum(mk)
# КОЛИЧЕСТВО ЗАЯВОК2(без тех кто удалился)
A12 = []
for z in A11:
    m,x = z
    k = 0
    for y in x:
        if isinstance(y,str):
            if y.count('Конкурсн')+y.count('конкурсн')>0:
                break
            else:
                k = k+1
        else:
            k = k+1
    if k == len(x):
        A12.append(z)
m = set()
# ВСЕ ЗАЯВКИ ПО НОМЕРАМ
A3 = []
for z in A12:
    k,x = z
    m.add(len(x))
    if isinstance(x[11],int):
        A3.append([x[1],x[11],k,x])
    else:
        A3.append([x[1],x[12],k,x])
A3 = sorted(A3)
A33 = sorted(A33)
print('Заявки / Люди / Олимпиадники / Бюджет без олимпиадников')
print(len(A3),len(A2),len(A01)+len(A00)//2,sk)
# Выводит сколько человек пойдут на какую специальность по согласиям, без повторений, по первейшему приоритету, выше 2 приоритета
### Баллы меня сам (z[3])
print("Номер / Количество выше с согласиями / коэфф попадания")
A1 = [[],[],[],[],[],[],[],[],[],[]]
my = set()
for f in A3:
    p,x,k,z = f
    if p<=5 and (x not in my) and (z[3]>262 or isinstance(z[4],str)) and len(z[2])>5:
        my.add(x)
        if len(A1[k])>=mk[k]:
            continue
        A1[k].append(z)
k = 0
sm = 0

for v in range(1,len(A1)):
    k = k+1
    print(k,len(A1[v]),(len(A1[v])//2)/mk[v])
    sm = sm+len(A1[v])
# Выводит сколько человек выше тебя по баллам по специальностям скорее всего куда поступят, без согласий
print('P.S.: Номер - номер как ты закидывал в файл, который первый закинул - 1, второй - 2 и тд')
print("Номер / Количество без учета согласий(//2) / коэфф попадания")
A19 = [[],[],[],[],[],[],[],[],[],[]]
myg = set()
for f in A3:
    p,x,k,z = f
    if p<=5 and (x not in myg) and (z[3]>262 or isinstance(z[4],str)):
        myg.add(x)
        if len(A19[k])>=mk[k]:
            continue
        A19[k].append(z)
k = 0
sm1 = 0
for v in range(1,len(A19)):
    k = k+1
    print(k,len(A19[v])//2,(len(A19[v])//2)/mk[v])
    sm1 = sm1+len(A19[v])//2
#Реальное количество согласий всего
kol = 1
k = 1
mg = set()
for v in range(0,len(A33)-1):
    k,x = A33[v]
    k1,x1 = A33[v+1]
    if len(x1)<13:
        continue
    if k==k1:
        k = k+1
        if isinstance(x[11],int):
            mg.add(x1[11])
        else:
            mg.add(x1[12])
    else:
        mg.add(x1[11])
        k = 1
        kol = kol+1
print("Количество согласий всего, даже тех кто ниже")
print(len(mg))
print("Количество согласий кто выше / Количество человек, которые выше(поделено на 2)")
print(sm,sm1)
print("Коэффициент попадания с согласиями / без")
print(sm/(sk+ko),sm1/(sk+ko))
print("Согласия одного человека(можно менять)")
k = 0
##for f in A3:
##    p,x,k,z = f
##    if x==2194547:
##        print(f)





        
