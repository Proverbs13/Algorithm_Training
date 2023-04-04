# dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
#
# key = input('키 입력 : ')
# val = input('밸류 입력 : ')
#
# dic[key] = val
#
# print(dic)

# 피보나치
# a=0
# b=1
# c=1
# n = int (input())
# for i in range (n-3):
#     a = b+c
#     c=b
#     b=a
# print(a)

#
# N=int(input())
# asd=[]
# asd=list(map(int, input().split()))
# asd.sort()
# maxval=max(asd)
# asd2 =[]
# for i in asd :
#     asd2.append(i/maxval *100)
# result = 0
# result = sum(asd2)
# result = result/N
# print(result)


# word = input().lower()
# lists = list(set(word))
# lists2 = []
# for i in lists:
#     count = word.count(i)
#     lists2.append(count)
#
# if lists2.count(max(lists2)) >= 2:
#     print("?")
# else:
#     print(lists[lists2.index(max(lists2))].upper())



# n,m=map(int,input().split())
# a=1
# for i in range (1,n+1):
#     a=a*i
# b=1
# for i in range (1,m+1):
#     b=b*i
# c=1
# for i in range (1,(n-m)+1):
#     c=c*i
#
# result= a//(b*c)
# print(result)

# 유클리드 호제법
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a

#나온 a는 최대공약수 , a*b 나누기 최대공약수는 최소공배수
#math모듈 gcd(a,b)

#에라토스테네스의 체
# def era(n):
#     num = [True]*(n+1) # 로 채워진 n+1개 리스트 만들기
#     for i in range (2*n+1):
#         if num[i]:
#             for  j in range(i, n+1):
#                 num[i*j]=False

#import sys
#sys.stdin.readline() 속도빠른입력 .rstrip 오른쪽 공백하나 int() 추가하면 정수만 일반적




######-9020

# import sys
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a
# a1,a2 = map(int,input().split())
# b1,b2 = map(int,input().split())
# c2= b2*a2
# c1= a1*b2 + a2*b1
# d=gcd(c2,c1)
# d1=c1//d
# d2=c2//d
# print(d1,d2)


##########-15965
# k=int(input())
# n=7400000
# a = [False,False] + [True]*(n-1)
# asd=[]
#
# for i in range(2,n+1):
#   if a[i]:
#     asd.append(i)
#     for j in range(2*i, n+1, i):
#         a[j] = False
#
# print (asd[k-1])
# n = int(sys.stdin.readline())




# ############-9020
# import sys
# N=10007
# a = [False,False] + [True]*(N-1)
# asd=[]
# for i in range(2,N+1):
#   if a[i]:
#     asd.append(i)
#     for j in range(2*i, N+1, i):
#         a[j] = False
#
# n = int(sys.stdin.readline())
# even=[]
# for i in range (n):
#     even.append(int(input()))
#
# answer=[]
# k=0
#
# for i in range (n):
#     j = 0
#     while True:
#         if even[i]-asd[j] in asd :
#             answer.append(asd[sj])
#         if asd[j] >= even[i] - asd[j]:
#             break
#         j+=1
#     a = answer.pop()
#     print(even[i]-a, a)
#     answer.clear()
#     k=0
#     a=0
# ###############################
# import sys
# N=10007
# a = [False,False] + [True]*(N-1)
# asd=[]
# for i in range(2,N+1):
#   if a[i]:
#     asd.append(i)
#     for j in range(2*i, N+1, i):
#         a[j] = False
# print(asd)
# n = int(sys.stdin.readline())
# even=[]
# for i in range (n):
#     even.append(int(input()))
# bgyo=[]
# answer=[]
# k=0
# for i in range (n):
#     while even[i] >= asd[k]:
#         bgyo.append(asd[k])
#         k+=1
#     for j in range (len(bgyo)):
#         if even[i]-bgyo[j] in bgyo and bgyo[j] <= even[i]-bgyo[j]:
#             answer.append(bgyo[j])
#             a = answer.pop()
#     print(a, even[i]-a)
#     bgyo.clear()
#     answer.clear()
#     k=0
#     a=0
# #############################
# import sys
# def is_prime(a):
#     for i in range(2, int(pow(a, 0.5)) + 1):
#         if a % i == 0:
#             return False
#     if a == 1:
#         return False
#     return True
# n = int(input())
# even=[]
# for i in range (n):
#     even.append(int(input()))
# for i in range (n):
#     a=even[i]/2
#     b=even[i]/2
#     while 1:
#         if is_prime(a) and is_prime(b):
#             print(int(a), int(b))
#             break
#         a-=1
#         b+=1

#################################

# n=int(input())
# a= [0 for i in range (n+2)]
# a[0]=1
# a[1]=1
# a[2]=1
# if n==1:
#     print (1)
# elif n==2:
#     print (1)
# elif n>=3:
#     for i in range(3,n+1):
#         a[i]=a[i-1]+a[i-2]
#     print(a[n])

#################################

# N=int (input())
# for i in range(N):
#     n = int(input())
#
#     if n== 0:
#         print(1,0)
#     elif n == 1:
#         print(0,1)
#     elif n == 2:
#         print(1,1)
#     elif n >= 3:
#         a = [0 for i in range(n + 2)]
#         a[0] = 1
#         a[1] = 1
#         a[2] = 1
#         for i in range(3, n + 1):
#             a[i] = a[i - 1] + a[i - 2]
#         print(a[n-1],a[n])
#         a.clear()

#########################################

# N=int(input())
# asd=[[0,0,0] for _ in range(N)]
# for i in range(N):
#     asd[i][0],asd[i][1], asd[i][2] = (map(int, input().split()))
#
#
# for i in range(N):
#     asd[i][0]+=min(asd[i-1][1],asd[i-1][2])
#
#     asd[i][1]+=min(asd[i-1][0],asd[i-1][2])
#
#     asd[i][2]+=min(asd[i-1][0],asd[i-1][1])
# print(min(asd[N-1]))
############################
# N=int(input())
# result1 = 0
# result2 = 0
# result3 = 0
#
# asd=[[0,0,0] for _ in range(N)]
# for i in range(N):
#     asd[i][0],asd[i][1], asd[i][2] = (map(int, input().split()))
# # print(asd[0].index(min(asd[0])))
# # print(min(asd[0]))
#
#
#
# for i in range(N):
#     if i == 0:
#         result1 += (asd[0][0])
#         store=0
#     elif asd[i].index(min(asd[i]))!=store:
#         result1 += min(asd[i])
#         store=asd[i].index(min(asd[i]))
#     else:
#         if store == 0:
#             result1 += min(asd[i][1], asd[i][2])
#             if min(asd[i][1], asd[i][2])==asd[i][1]:
#                 store = 1
#             else:
#                 store = 2
#         elif store == 1:
#             result1 += min(asd[i][0], asd[i][2])
#             if min(asd[i][0], asd[i][2])==asd[i][0]:
#                 store = 0
#             else:
#                 store = 2
#         else:
#             result1 += min(asd[i][0], asd[i][1])
#             if min(asd[i][1], asd[i][0])==asd[i][1]:
#                 store = 1
#             else:
#                 store = 0
# for i in range(N):
#     if i == 0:
#         result2 += (asd[0][1])
#         store=1
#     elif asd[i].index(min(asd[i]))!=store:
#         result2 += min(asd[i])
#         store=asd[i].index(min(asd[i]))
#     else:
#         if store == 0:
#             result2 += min(asd[i][1], asd[i][2])
#             if min(asd[i][1], asd[i][2])==asd[i][1]:
#                 store = 1
#             else:
#                 store = 2
#         elif store == 1:
#             result2 += min(asd[i][0], asd[i][2])
#             if min(asd[i][0], asd[i][2])==asd[i][0]:
#                 store = 0
#             else:
#                 store = 2
#         else:
#             result2 += min(asd[i][0], asd[i][1])
#             if min(asd[i][1], asd[i][0])==asd[i][1]:
#                 store = 1
#             else:
#                 store = 0
# for i in range(N):
#     if i == 0:
#         result3 += (asd[0][2])
#         store=2
#     elif asd[i].index(min(asd[i]))!=store:
#         result3 += min(asd[i])
#         store=asd[i].index(min(asd[i]))
#     else:
#         if store == 0:
#             result3 += min(asd[i][1], asd[i][2])
#             if min(asd[i][1], asd[i][2])==asd[i][1]:
#                 store = 1
#             else:
#                 store = 2
#         elif store == 1:
#             result3 += min(asd[i][0], asd[i][2])
#             if min(asd[i][0], asd[i][2])==asd[i][0]:
#                 store = 0
#             else:
#                 store = 2
#         else:
#             result3 += min(asd[i][0], asd[i][1])
#             if min(asd[i][1], asd[i][0])==asd[i][1]:
#                 store = 1
#             else:
#                 store = 0
#
# print(result1)
# print(result2)
# print(result3)
#
# print(min(result1,result2,result3))
#

########
#
# import sys
# N=1005000
# a = [False,False] + [True]*(N-1)
# asd=[]
# for i in range(2,N+1):
#   if a[i]:
#     asd.append(i)
#     for j in range(2*i, N+1, i):
#         a[j] = False
#
# n = int(sys.stdin.readline())
# i=0
# while True:
#     if asd[i]>=n :
#         break
#     i+=1
#
# while True:
#     x=asd[i]
#     x=str(x)
#     tmp=x[::-1]
#     if x==tmp:
#         break
#     i+=1
# print(asd[i])
##############################파도반수열
# import sys
# n = int(sys.stdin.readline())
# p=[1,1,1,2,2,3,4,5,7,9]
#
# for i in range (10,102):
#     p.append(p[i-2]+p[i-3])
#
# for i in range(n):
#     n1 = int(sys.stdin.readline())
#     print (p[n1-1])
########################################lcs
# str1=input()
# str2=input()
# l1=len(str1)
# l2=len(str2)
# a = []
#
# for i in range(l2+1):
#     line = []
#     for j in range(l1+1):
#         line.append(0)
#     a.append(line)
#
# for i in range(1,l2+1):
#     for j in range(1,l1+1):
#         if str1[j-1] != str2[i-1]:
#             a[i][j]=max(a[i-1][j],a[i][j-1])
#         else:
#             a[i][j] = a[i - 1][j-1]+1
# print (a[-1][-1])




# if str1[j] == str2[i]:
#     a[i][j] += 1
#     k = j + 1
#     if check == 0:
#         while k < l1:
#             a[i][k] += 1
#             k += 1
#         check += 1
#     break
#
# if i < l2 - 1:
#     for f in range(l1):
#         a[i + 1][f] = a[i][f]
# check = 0






# ###########빈도정렬
# from collections import OrderedDict
#
# N ,K= map(int, input().split())
#
#
# asd=list(map(int, input().split()))
#
# asd2 = list()
# asd2=asd.copy()
#
# asd2= list (OrderedDict.fromkeys(asd2))
#
#
# countlist = [0 for i in range(len(asd2))]
#
# count= 0
#
# for i in range (len(asd2)):
#     for j in range (N):
#         if asd2[i] == asd[j]:
#             count +=1
#             asd[j]=-1
#     countlist[i]=count
#     count=0
#
# # print (asd2)
# # print (countlist)
#
# result=[]
#
# for i in range( len(asd2)):
#     result.append([countlist[i],asd2[i]])
#
#
# for i in range(len(result)):
#         for j in range(len(result)-1):
#             if result[j][0]<result[j+1][0]:
#                 result[j], result[j + 1] = result[j + 1], result[j]
# # print (result)
#
# for i in range(len(result)):
#     for j in range(result[i][0]):
#         print(result[i][1],end=" ")

# ##### 수정렬하기 3
#
# N = int(input())
# asd = [0] * 10003
# for i in range(N):
#     asd[i]=int(input())
# asd2=asd[0:N]
#
# asd2.sort()
# for i in range(0,N):
#     print(asd2[i])

##### 수정렬하기 3

# ##RGB 거리
# N = int(input())
# asd = [[0, 0, 0] for _ in range(N)]
# for i in range(N):
#     asd[i][0], asd[i][1], asd[i][2] = (map(int, input().split()))
#
# for i in range(1, N):
#     asd[i][0] += min(asd[i - 1][1], asd[i - 1][2])
#
#     asd[i][1] += min(asd[i - 1][0], asd[i - 1][2])
#
#     asd[i][2] += min(asd[i - 1][0], asd[i - 1][1])
# print(min(asd[N - 1]))


# 소트인사이트
# n=str(input())
# int_n=int (n)
# a= len(n)
# list=[]
#
# for i in range( 0,a):
#     list.append(int(n[i: i + 1]))
# list.sort()
# list.reverse()
# for i in list:
#     print(i, end='')

# #터렛
# n= int (input())
# for i in range (0,n):
#     asd1 = list(map(int, input().split()))
#
#     x1 = asd1[0]
#     y1 = asd1[1]
#     r1 = asd1[2]
#     x2 = asd1[3]
#     y2 = asd1[4]
#     r2 = asd1[5]
#
#     cm=((x1-x2)**2 + (y1 -y2)**2 )** (1/2)
#
#
#     if ((cm==0) and (r1 == r2)):
#         print("-1")
#     elif ( cm == (r1 + r2) ):
#         print("1")
#     elif ((cm == abs(r1 - r2)) ):
#         print("1")
#     elif (  abs(r1-r2) < cm < (r1 + r2)):
#         print("2")
#     else:
#         print("0")

#1026
# n= int (input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# A.sort()
# B.sort()
# B.reverse()
# c = 0
# for i in range(0,n):
#     c+= A[i] * B[i]
# print (c)




# # #피보나치 확장
# a=1
# b=1
# c=1
# s=0
# n = int (input())
#
#
# if n>0:
#     for i in range(n - 2):
#
#         a = b % 1000000000 + c % 1000000000
#         c = b % 1000000000
#         b = a % 1000000000
#
#
#     if a > 0:
#         print("1")
#     elif a == 0:
#         print("0")
#     else:
#         print("-1")
#     s = abs(a) % 1000000000
#     print(s)
#
# if n<=0:
#
#     a = 1
#     b = -1
#     c= 2
#     for i in range(0,(-n)+2):
#         a = b% 1000000000 + c% 1000000000
#         c = b% 1000000000
#         b = a% 1000000000
#
#
#     if ((-n) % 2 == 0):
#         a = -a
#     if (n== 0):
#         a = 0
#
#     if a > 0:
#         print("1")
#     elif a == 0:
#         print("0")
#     else:
#         print("-1")
#
#
#     s = abs(a) % 1000000000
#     print(s)

# #Fly me to the Alpha Centauri
# n=int(input())
# for i in range(n):
#      a,b=(map(int, input().split()))
#      s = b-a
#      i = 1
#      count = 0
#
#      while 1:
#          s = s - 2 * i
#          count += 1
#          if s <= 0:
#              s = s + 2 * i
#              break
#          i += 1
#
#      if s == 0:
#          count = count * 2
#      elif s - i > 0:
#          count = count * 2
#      else:
#          count = count * 2 - 1
#      print(count)

# 삼성 아카데미 최소이동으로 값 바꾸기 문제
#N= int(input())
#
# a,n = (map(int,input().split()))
# a=str(a)
# lenA=len(a)
# list=[]
# for i in range(lenA):
#     list.append(a[i:i+1])
#
#
# min=0
# count=0
# tmp = 0
# max_index = 1
# check = 0
#
# for i in range (n):
#     max=list[]
#     max_index=i
#     check= 0
#     for j in range (len(list)):
#         if max <= list[j]:
#             max_index=j
#             max= list[j]
#             check+=1
#
#     if (check !=0):
#         tmp = list[max_index]
#         list[max_index] = list[i]
#         list[i] = tmp
#     else:
#         tmp = list[len(list)-1]
#         list[len(list)-1] = list[len(list)-2]
#         list[len(list)-2] = tmp
#
# print (list)


#어퍼 바꾸기
# s=input()
# s.upper()
# b=list(s)
# s=[]

# for i in range(len(b)):
#     a=b[i]
#     a=str(a)
#     a=a.upper()
#     s.append(a)

# for i in range(len(s)):
#     print(s[i],end='')






# for i in range (1,5000):
#     t = 0
#     for j in range(1, i):
#         t += 2 * (j)
#     t = t + i
#     list.append(t)
# list[0]= 2
# print (list)

# #외로운 문자
# N= int(input())
# list_str =[]
# for t in range(N):
#     s = input()
#     list_str.append(s)
#
# for t in range(N):
#     b = list(list_str[t])
#     a = set(b)
#     a = list(a)
#     a_count = []
#     for i in range(len(a)):
#         a_count.append(0)
#     count = 0
#
#     for i in range(len(list_str[t])):
#         for j in range(len(a)):
#             if b[i] == a[j]:
#                 a_count[j] += 1
#     a.sort()
#
#     print("#", end="")
#     print(t + 1, end=" ")
#     for j in range(len(a)):
#
#         if (a_count[j] == 1):
#
#             print(a[j], end="")
#             count += 1
#     if count == 0:
#         print("Good", end="")
#     print("")
# # 6
# # xxyyzz
# # yc
# # aaaab
# # bca
# # ppzqq
# # qnwerrewmq


# #OXOOXOXO
# N=int(input())
# l=[]
# for j in range(N):
#     s = input()
#     a = list(s)
#     count = 1
#     result = 0
#
#     if a[0] == 'O':
#         result += count
#
#     for i in range(1, len(s)):
#         if a[i] == 'O':
#             if a[i - 1] == 'O':
#                 count += 1
#                 result += count
#             else:  # x 일때
#                 count = 1
#                 result += count
#         else:
#             count = 1
#     l.append(result)
#
#
# for j in range(N):
#     print("#",end="")
#     print(j+1,end=" ")
#     print(l[j])

# 분수찾기
# N= int(input())
# n=N
# i=1
# 
# while 1:
#     n=n-i
#     if(n<=0):
#         break
#     i += 1
# n+=i
# if i%2==0:
#     print(1 + (n - 1), end="")
#     print("/", end="")
#     print((i - (n - 1)), end="")
# else:
#     print((i - (n - 1)), end="")
#     print("/", end="")
#     print(1 + (n - 1), end="")



# #토마토
# ga,se = (map(int,input().split()))
# arr= [[0]*(ga+1) for i in range(se+1)]
#
# day =0
# for i in range(1,se+1):
#     arr[i]=list(map(int, input().split()))
# 아직다못함


# A+B - 4
# while 1:
#     try:
#         a, b = map(int, input().split())
#         print(a + b)
#
#     except :
#         break


# #부녀회장이 될테야
#
# N=int(input())
# for i in range(N):
#     k = int(input())
#     n = int(input())
#
#     result = 0
#     arr = [[0] * (n) for i in range(k + 1)]
#     add = 1
#
#     if k == 0:
#         print(n)
#     else:
#         for i in range(n):
#             arr[0][i] = add
#             add += 1
#             result = 0
#
#         for i in range(k):
#             arr[i][0] == 1
#
#         for i in range(1, k + 1):
#             for j in range(n):
#                 arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
#                 result = arr[i][j]
#
#         print(arr[k][n - 1])



# 팰린드롬수
# while 1:
#     N = str(input())
#     if N=="0":
#         break
#     if N == N[::-1]:
#         print("yes")
#     else:
#         print("no")

# #2진수 8진수
#
# N = (input())
# int_N= int(N)
# N=list(N)
# N.reverse()
# result=0
# ad=2
# if int_N==0:
#     print("0")
#
# else:
#     for i in range(len(N)):
#         result += (2 ** i) * int(N[i])
#
#     a = 0
#     asd = []
#     while (result != 0):
#         a = result % 8
#         asd.append(a)
#         result //= 8
#
#     asd.reverse()
#     for i in range(len(asd)):
#         print(asd[i], end="")
# print(oct(int(input(),2))[2:])


# #1로 만들기
# #인덱스 i = 이동횟수
# N = int(input())
# count = 0
# a=[0 for i in range (N+1)]
#
# for i in range(2, N+1):
#     a[i] = a[i - 1] + 1
#     if i%3 ==0:
#         a[i]= min(a[i-1]+1,a[i//3]+1)
#     if i%2==0:
#         a[i]= min(a[i-1]+1,a[i//2]+1)
# print(a[N])

# # 방번호
# N= (input())
# a=list(N)
# tmp=0
# namu =0
# b= [0 for i in range(10)]
# for i in range(len(a)):
#     if int(a[i])==6 or int(a[i])==9:
#         if b[6] > b[9]:
#             b[9] += 1
#         else:
#             b[6] += 1
#     else:
#         b[int(a[i])] += 1
# print(max(b))

# # #숫자의 개수
# N1= int(input())
# N2= int(input())
# N3= int(input())
# s=N1*N2*N3
# a=[]
# s=str(s)
# a=list(s)
#
# b= [0 for i in range(10)]
# for i in range(len(a)):
#     b[int(a[i])] +=1
# for i in range(10):
#     print(b[i])


# #표절
# N= int(input())
# asd= list(map(int, input().split()))
# asd.sort()
# t=0
# count = 0
# for i in range (N):
#     first = i
#     last = N-1
#     while first<=last:
#         m= (first + last)//2
#         if asd[i] < 0.9*asd[m]:
#             last = m - 1
#         else:
#             first = m + 1
#     count+= last - i
# print(count)


# import sys
# #신입사원
# input=sys.stdin.readline
# n2=int(input())
#
# for i in range(n2):
#     result=1
#     N = int(input())
#     a = []
#     c = [0, 0]
#     for i in range(N):
#         c = list(map(int, input().split()))
#         a.append(c)
#     a.sort()
#     mint = a[0][1]
#     for i in range(1, N):
#         if (a[i][1] <mint):
#             mint = a[i][1]
#             result += 1
#     print(result)


# #피보나치 수의 개수
# import sys
# input=sys.stdin.readline
#
# while 1:
#     a, b, c = 0, 1, 1
#     A, B = map(int, input().split())
#     count = 0
#     check = 0
#     if A==0 and B==0:
#         break
#     if A==0 or A==1:
#         count+=1
#     while 1:
#         if (B < a):
#             break
#         a = b + c
#         c = b
#         b = a
#         if (B >= a and a >= A):
#             count += 1
#     print(count)


# # 어린왕자
# import sys
# input=sys.stdin.readline
#
# for i in range (int(input())):
#     count=0
#     x1, y1, x2, y2, = map(int, input().split())
#     pla=[]
#     for j in range(int(input())):
#         pla.append(list(map(int, input().split())))
#     for i in range (len(pla)):
#         ds1= ((x1-pla[i][0])**2 + (y1-pla[i][1])**2)**(1/2)
#         ds2= ((x2-pla[i][0])**2 + (y2-pla[i][1])**2)**(1/2)
#         r= pla[i][2]
#         if (ds1<r) and (ds2<r):
#             continue
#         elif (ds1>r)and(ds2>r):
#             continue
#         else:
#             count+=1
#     print(count)


# # 접두사
# import sys
# input=sys.stdin.readline
# N=int(input())
# w=[]
# for i in range(N):
#     w.append(input().rstrip())
# check=0
# w= list(set(w))
# tmp = w[:]
# count=len(w)
# for i in range(len(w)):
#     for j in range(len(w)):
#         if j!=i and len(w[j])>=len(tmp[i]):
#             #print(w[j][0:len(tmp[i])], tmp[i])
#             if w[j][0:len(tmp[i])] == tmp[i]:
#                 count-=1
#                 break
# print (count)


# # 영화감독 숌
# import sys
# input=sys.stdin.readline
# n=int(input())
# count=0
# s=0
# while 1:
#     s+=1
#     if "666" in str(s):
#         count+=1
#     if n == count:
#         print(s)
#         break


# #단어수학
# import sys
# input=sys.stdin.readline
# #alpa=[[0,"A"],[0,"B"],[0,"C"],[0,"D"],[0,"E"],[0,"F"],[0,"G"],[0,"H"],[0,"I"],[0,"J"]]
# N=int(input())
# ipstr=[0 for _ in range(N)]
# s=""
# for i in range(N):
#     ipstr[i]=input().rstrip()
#     s+=ipstr[i]
# s=sorted(list(set(list(s))))
# alpa=[]
# for i in range(len(s)):
#     alpa.append([0,s[i]])
#
# for k in range(len(ipstr)):
#     for i in range(len(ipstr[k])):
#         for j in range(len(alpa)):
#             if ipstr[k][i] == alpa[j][1]:
#                 alpa[j][0] += 10 ** (len(ipstr[k]) - i)
# alpa.sort()
# alpa.reverse()
# add=9
# for i in range(len(alpa)):
#     alpa[i][0]=add
#     add-=1
# result=0
# for k in range(len(ipstr)):
#     for i in range(len(ipstr[k])):
#         for j in range(len(alpa)):
#             if ipstr[k][i] == alpa[j][1]:
#                 result += (10 ** (len(ipstr[k]) - i-1)) * alpa[j][0]
# print (result)


# #숫자 연결하기
# import sys
# input=sys.stdin.readline
# n,k= map(int, input().split())
# jump=len(str(n))
# firstn = n
# count=1
# modulo=[0 for i in range (k)]
# # k에서 1~(k-1) 가지 나머지가 다나오고 끝남+
# # 그외에 나왔던게 또나오면 -1
# # 진짜 앞에 더하고 나머지구하면 시간 터짐
# # 그러므로 모듈러 연산 성질 이용해야함
# m=n%k
# b_m =0
# while 1:
#     if m==0:
#         print(count)
#         break
#
#     if  modulo[m]==1:
#         print("-1")
#         break
#     modulo[m]=1
#     # print((m * (10 ** (len(str(n))))) + firstn)
#     m=((m*(10**(len(str(n))))) +firstn) %k
#     count += 1


# #DNA
# import sys
# input=sys.stdin.readline
# N,M=map(int, input().split())
# dna=[]
# for i in range(N):
#     dna.append(input().rstrip())
# dnalist=[["T",0],["A",0],["C",0],["G",0]]
# resultlist=[0 for i in range(M)]
# MAXQWE=0
# MAXASD=["z","z","z","z"]
# for i in range(M): #라인변경
#     for j in range(N): # 아래라인으로 탐색
#         for k in range(4): #4개중에있는지
#             if dna[j][i]==dnalist[k][0]:
#                 dnalist[k][1]+=1
#
#     dnalist = sorted(dnalist, key=lambda x: x[1])
#     dnalist.reverse()
#     MAXQWE =dnalist[0][1]
#     for k in range(4):  # 4개중에있는지
#         if MAXQWE == dnalist[k][1]:
#             MAXASD[k]= dnalist[k][0]
#     MAXASD.sort()
#     resultlist[i]=MAXASD[0]
#
#     for k in range(4):
#         dnalist[k][1]=0
#         MAXASD[k]="z"
#
# result = ''.join(s for s in resultlist)
# print(result)
#
# count=0
# for i in range(N): #라인변경
#     for j in range(M): # 아래라인으로 탐색
#         if dna[i][j]!=resultlist[j]:
#             count+=1
# print(count)


# #주사위 세개
# import sys
# input=sys.stdin.readline
# dice=[0,0,0]
# dice[0],dice[1],dice[2] = map(int, input().split())
# result=0
# dice_set=list(set(dice))
# dice.sort()
# if len(dice_set)==1:
#     result=dice[0]*1000 +10000
# elif len(dice_set)==2:
#     if dice[1]==dice[0]:
#         result = 1000+ (dice[0] * 100)
#     else :
#         result = 1000+ (dice[2] * 100)
# else:
#     result= 100* dice[2]
# print(result)


# #분산처리
# import sys
# input=sys.stdin.readline
# ablist=[]
# N=int(input())
# for i in range(N):
#     ablist.append(list(map(int, input().split())))
# for i in range(N):
#     tmp =ablist[i][0]
#     jump = 1
#     resultlist=[]
#     while 1:
#         tmp=(ablist[i][0]**(jump))%10
#         if jump>=2 and  (ablist[i][0])%10 == tmp:
#             jump-=1
#             break
#         jump += 1
#         resultlist.append(tmp)
#     if ablist[i][0]%10==0:
#         print("10")
#     else:
#         print(resultlist[  (ablist[i][1]%jump)-1   ])



# # #분산처리
# import sys
# import math
# input=sys.stdin.readline
# A,B,N =map(int, input().split())
# result=A/B
# result=math.floor((result*(10**N))%10)
# print(result)


# 크냐
# while 1:
#     N, M = map(int, input().split())
#     if N==0 and M ==0:
#         break
#     if (N > M):
#         print("Yes")
#     else:
#         print("No")


# # 음식평론가
# import sys
# input=sys.stdin.readline
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a
# N,M = map(int, input().split())
# print(M-gcd(N,M))


# #
# import sys
# input=sys.stdin.readline
#
# a=[x**2 for x in range (7) if x%3==0 ]
# print(a)
#
# list_b = [i for i in range(7) if i > 5]
# print(list_b)


# # 1182 부분수열의 합
# import sys
# input=sys.stdin.readline
# count = 0
# a=[]
# N, S = map(int, input().split())
# for i in range (N):
#     a.append(int(input().rstrip()))
#
# for i in range(N):
#     if a[i]==S:
#         count+=1;
#         print("!!!")
#
# i=0
# for i in range(0,N):
#     d=1
#     while(i+d<N):
#         print (a[i],a[i+d],a[i]+a[i+d])
#         if S==a[i]+a[i+d]:
#             count+=1
#             print("!!!!")
#         d+=1
# print(count)
#
# a=[]
# N, S = map(int, input().split())
# a=list(map(int, input().split()))
# print (a)
#
# n=[]
# for i in range( N):
#     a[i]


# # 핸드폰 요금
# import sys
# input=sys.stdin.readline
# N=int(input())
# a = list(map(int, input().split()))
# ry=[]
# t=0
# for i in range(N):
#     if a[i]<30:
#         ry.append(10)
#     else:
#         t = a[i] - (30 * (a[i] // 30))
#         if (t >= 0):
#             ry.append((a[i] // 30 * 10) + 10)
#         else:
#             ry.append((a[i] // 30 * 10))
#     t = 0
#
# rm=[]
# t=0
# for i in range(N):
#     if a[i]<60:
#         rm.append(15)
#     else:
#         t = a[i] - (60 * (a[i] // 60))
#         if (t >= 0):
#             rm.append((a[i] // 60 * 15) + 15)
#         else:
#             rm.append((a[i] // 60 * 15))
#     t = 0
# #print("y=",sum(ry),"M=",sum(rm))
# y=sum(ry)
# m=sum(rm)
# if y < m:
#     print("Y", y)
# elif y > m:
#     print("M", m)
# else :
#     print("Y","M", m)

# # 3의배수
# import sys
# input=sys.stdin.readline
#
#
# a =str(int(input()))
# count=0
# while 1:
#     b = 0
#     if len(a)==1:
#         if int(a) % 3 == 0:
#             print(count)
#             print("YES")
#             break
#         else:
#             print(count)
#             print("NO")
#             break
#     for i in a:
#         b += int(i)
#     a = str(b)
#     count += 1



# # 방학숙제
# import sys
# input=sys.stdin.readline
#
# L=int(input())
# A=int(input()) # 국어
# B=int(input()) # 수학
# C=int(input()) # 국어 최대
# D=int(input()) # 수학 최대
#
# if A%C !=0:
#     na=A//C + 1
# else:
#     na=A//C
# if B%D !=0:
#     nb=B//D + 1
# else:
#     nb=B//D
# #print ("na",na,"nb",nb)
# print(L-max(nb,na))

# # 문자열 반복복
# import sys
# input=sys.stdin.readline
#
# for i in range(int(input())):
#     N,sN = input().split()
#     N=int(N)
#     for j in sN:
#         print(N*j,end ="")
#     print()

# # 체스판 다시 칠하기
# import sys
# input=sys.stdin.readline
#
# M,N = map(int,input().split())
# arr = []
# for i in range(M):
#     arr.append(str(input()).rstrip())
#
# cntw=0 # 시작이 화이트
# cntb=0 # 시작이 블랙
#
# R=[]
#
# for a in range( 0,M-7):
#     for b in range( 0,N-7):
#         cntw = 0
#         cntb = 0
#         for i in range(a, a + 8):
#             for j in range(b,b+8):
#                 if (i+j)%2 == 0:
#                     # 그 순간 타일위치합 짝수일때 처음 모양이랑 같아야함
#                     if arr[i][j]!='W':
#                         cntw +=1
#                     else:
#                         cntb +=1
#                 else:
#                     if arr[i][j]!='B':
#                         cntw +=1
#                     else:
#                         cntb +=1
#         R.append(min(cntw,cntb))
#
# print(min(R))

# # 소수구하기
# import sys
# input=sys.stdin.readline
#
# a,b=map(int,input().split())
# N=[]
# N.append(0)
# for i in range( 1,1000001):
#     N.append(i)
# for i in range( 2,b):
#     if N[i]!=0:
#         for j in range(2*i,1000001,i):
#             N[j]=0
# N[1]=0
#
# for i in range( a,b+1):
#     if N[i]!=0:
#         print(N[i])

# # 직사각형에서 탈출
# import sys
# input=sys.stdin.readline
# x,y,w,h = map(int,input().split())
# print(min(x,w-x,y,h-y))

# # 설탕 배달 - dp
# import sys
# input=sys.stdin.readline
# N=int(input())
# a=[5001 for i in range(5001)]
# a[3]=a[5]=1
# for i in range(6, N+1):
#     a[i]= min(a[i-3]+1,a[i-5]+1)
# if a[N]>=5001:
#     print(-1)
# else:
#     print(a[N])

# # 설탕 배달 - 그리디
# import sys
# input=sys.stdin.readline
# N=int(input())
# cnt=0
# while N>=0:
#     if N%5==0:
#         cnt+=N//5
#         print(cnt)
#         t=1
#         break
#     N-=3
#     cnt+=1
# if N<0:
#     print(-1)

# #평범한 배낭
# import sys
# input=sys.stdin.readline
#
# N, K = map(int, input().split())
# a = [[]]
# back = [[0 for i in range(K + 1)] for j in range(N + 1)]
#
# for i in range(N):
#     a.append(list(map(int, input().split())))
#
# for i in range( 1,N+1):
#     for j in range( 1, K+1):
#         w=a[i][0] # 물건무게
#         v=a[i][1] # 물건가치
#         if j<w: # 가방무게가 물건무게보다 적을때
#             back[i][j]= back[i-1][j]
#         else :
#             back[i][j] = max( back[i-1][j] , v+ back[i-1][j-w] )
#             #이전요소존재할때 최대값이랑,
#             #현재요소 + 남은 무게로 이전에 넣을수있는거와의 합중에 가치 최대
# print(back[N][K])

# #부호
# import sys
# input=sys.stdin.readline
# R=[]
# for i in range(3):
#     a=[]
#     for j in range(int(input())):
#         a.append(int(input()))
#     S=sum(a)
#     if S>0:
#         R.append("+")
#     elif S==0:
#         R.append("0")
#     else:
#         R.append("-")
# for i in R:
#     print(i)

# #한수
# import sys
# input=sys.stdin.readline
# N=(str(int(input())))
# R=0
# cnt=0
# if int(N)<100:
#     R=int(N)
#     print(R)
# elif len(N)==3:
#     R += 99
#     for i in range(100,int(N)+1):
#         t=str(i)
#         if int(t[1])-int(t[0]) == int(t[2])-int(t[1]):
#             R+=1
#     print(R)
# else:
#     print("144")




# #윾유기농 배추
# import sys
# input=sys.stdin.readline
# sys.setrecursionlimit(10000)# 재귀제한해제
# def dfs(x,y):
#     g[y][x]=-99
#     dx=[0,0,1,-1]
#     dy=[1,-1,0,0]
#     for i in range(4):
#         nx= x+dx[i]
#         ny= y+dy[i]
#         if 0<=nx<M and 0<=ny<N:
#             if g[ny][nx]==1:
#                 g[ny][nx] == -99
#                 dfs(nx,ny)
# T=int(input())
# for i in range(T):
#     M, N, K = map(int, input().split())
#     cnt = 0
#     g = [[0 for i in range(M)] for j in range(N)]
#
#     for i in range(K):
#         X, Y = map(int, input().split())
#         g[Y][X] = 1
#
#     for i in range(N):
#         for j in range(M):
#             if g[i][j] == 1:
#                 dfs(j, i)
#                 cnt += 1
#     print(cnt)
#     #print(g)

# #상근날드
# import sys
# input=sys.stdin.readline
# a=[]
# b=[]
# for i in range(3):
#     a.append(int(input()))
# for i in range(2):
#     b.append(int(input()))
# print((min(a)+min(b))-50)


# #빠른 A+B
# import sys
# input=sys.stdin.readline
#
# for i in range( int(input())):
#     M, N = map(int, input().split())
#     print (M+N)


# # 대회 or 인턴
# import sys
# input=sys.stdin.readline
#
# N, M, K = map(int, input().split())
# while K>0:
#     if N > 2 * M :
#         N-=1
#     elif N < 2* M :
#         M-=1
#     else :
#         M-=1
#     K-=1
# # print ( N, M , K)
# if (M==0):
#     print (0)
# elif ( N >= 2*M ) :
#     print (M)
# else:
#     print(N//2)



# # 30
# import sys
# input=sys.stdin.readline
#
# N= str(int (input()))
# lenN= len(N)
# N=list(N)
# N = list(map(int, N))
#
# N.sort(reverse=True)
# if ( N[lenN-1] != 0 ):
#     print("-1")
#
# else:
#     if sum(N)%3==0:
#         N=list(map(str, N))
#         print(''.join(N))
#         # print(N)
#     else:
#         print("-1")

# # 평행사변형
# import sys
# input=sys.stdin.readline
#
# def length (xa,ya, xb,yb):
#     return ((xa - xb)**2 + (ya - yb)**2 )**(1/2)
#
# xa,ya,xb,yb,xc,yc = map(int,input().split())
#
# if (xb-xa)*(yc-ya)==(yb-ya) * (xc-xa):
#     print(-1.0)
# else:
#     a = []
#     a.append(length(xa, ya, xb, yb))
#     a.append(length(xb, yb, xc, yc))
#     a.append(length(xc, yc, xa, ya))
#     a.sort()
#     print(2 * (a[2] - a[0]))


# # 랜선자르기
# import sys
# input=sys.stdin.readline
#
# K,N = map(int,input().split())
# a=[]
# for i in range(K):
#     a.append(int(input()))
# a.sort(reverse=True)
# bot= 1
# top= a[0]
# while bot<=top:
# #정답 봇=탑 이라서 중앙에 딱 값을 찾을떄까지
#     mid = (bot + top) // 2
#     #print("mid=", mid)
#     temp = 0
#     for i in a:
#         temp+=i//mid
#     # if temp== N:
#     #     break
#     if temp < N:
#         top= mid-1
#     else: #temp>N
#         bot = mid+1
#     #print ("temp=",temp)
# print(top)

# #단어 뒤집기 1
# import sys
# #input=sys.stdin.readline
# for i in range(int(input())):
#     stack = []
#     b = []
#     a = input()
#
#     a = list(a)
#     i = 0
#     total = len(a)
#     a.append(" ")
#     a.append(" ")
#     # print(a)
#     # print("total=",total)
#
#     while total >= i :
#         if a[i] == ' ' :
#             i += 1
#             b.append(" ")
#             while a[i] != " ":
#                 t = a[i]
#                 stack.append(t)
#                 i += 1
#             # print ("stack=",stack)
#             for j in range(len(stack)):
#                 b.append(stack.pop())
#         elif i==0:
#             while a[i] != " ":
#                 t = a[i]
#                 stack.append(t)
#                 i += 1
#             # print ("stack=",stack)
#             for j in range(len(stack)):
#                 b.append(stack.pop())
#         else:
#             b.append(a[i])
#             i += 1
#         # print(b)
#         # print("i=",i)
#
#     b = ''.join(b)
#     print(b)
#


# #단어 뒤집기 2
# import sys
# #input=sys.stdin.readline
# stack=[]
# b=[]
# a=list(input())
# total=len(a)
# a.append("???") # 엔딩 확인용
# i=0
#
# while  total != i:
#     if a[i]=='<':
#         b.append(a[i])
#         i+=1
#         #print(i)
#         while a[i]!=">":
#             b.append(a[i])
#             i+=1
#         b.append(a[i])
#         i += 1
#
#
#     else:
#         while a[i] != "<" and a[i] !=" "and a[i] !="???":
#             stack.append(a[i])
#             i += 1
#         # print ("stack=",stack)
#         for j in range(len(stack)):
#             b.append(stack.pop())
#         if a[i]==" ":
#             b.append(" ")
#             i+=1
#
#     #print("i=",i)
#     #print("b=",b)
#
# b = ''.join(b)
# print(b)

# #괄호
# import sys
# #input=sys.stdin.readline
#
# for i in range(int(input())):
#     a=list(input())
#     sum = 0
#     length=len(a)
#     for j in range(length):
#         if a[j]=='(':
#             sum+=1
#         else :
#             sum-=1
#         if sum < 0:
#             print("NO")
#             break
#     if sum>0:
#         print("NO")
#     elif sum==0:
#         print("YES")

# #단어 길이재기
# import sys
# #input=sys.stdin.readline
# print(len(input()))

# #요세푸스 문제
# import sys
# #input=sys.stdin.readline
# N,K= map(int,input().split())
# a=[]
# result=[]
# for i in range(1,N+1):
#     a.append(i)
# #print("a ", a)
# t=K-1
# maxl=N
# for i in range(N):
#     result.append(a.pop(t))
#     if maxl==1:
#         maxl=1
#     else:
#         maxl-=1
#     t=(t+K-1)%(maxl)
#     #print(a)
#     #print("maxl",maxl)
#     #print("t",t)
# #print(result)
#
# #출력형식
# print("<",end="")
# for i in range(len(result)-1):
#     print(result[i],end=", ")
# print(result[N-1],end="")
# print(">")

# # 스택 수열
# import sys
# #input=sys.stdin.readline
# N= int(input())
# stack=[]
# ans=[]
# t=1
# for i in range(N):
#     pre = int(input())
#     while t<=pre:
#         stack.append(t)
#         ans.append("+")
#         t+=1
#     if stack[-1] == pre:
#         stack.pop(-1)
#         ans.append("-")
#     else:
#         print("NO")
#         ans.clear()
#         break
# for i in (ans):
#     print(i)

# # 에디터
# import sys
# #input=sys.stdin.readline
# #stack1 과 stack2로 구별해서 둘로 나눠 풀기 단순 insert 로는 시간초과남
# stack1=list(input())
# stack2=[]
# N=int(input())
# for i in range(1,N+1):
#     pre=list(input().split())
#     if pre[0]== "L":# 커서 왼쪽 이동
#         if stack1:
#             stack2.append(stack1.pop()) #오른쪽 스택으로 왼쪽스택의 요소이동
#     elif pre[0]=="P":
#         stack1.append(pre[-1])
#     elif pre[0]=="D": # 커서 오른쪽 이동
#         if stack2:
#             stack1.append(stack2.pop()) # 왼쪽 스택으로 오른쪽스택의 요소 이동
#     else :
#         if stack1:
#             stack1.pop()
#
# stack2.reverse() # 마지막에 있어야하는게 리스트 순서상 앞에있었으므로 뒤집기
# stack1 = stack1+ stack2
# stack1 = ''.join(stack1)
# print(stack1)

# # 탑
# import sys
# N=int(input())
# tower=list(map(int,input().split()))  # 타워 크기들 저장
# #print(tower)
# stack=[] # [인덱스, 높이] 들을 추가
# result=[]  #정답 리스트 저장
#
# for i in range(N):
#     #print ("i=",i)
#     if stack:
#         while stack:
#             if tower[i] > stack[-1][1]: # 현재 내 타워보다 높은거 마지막 저장타워에 었을 때
#                 stack.pop()  # 높은거나올때까지 팝 -> 어짜피 내가 높으면 날려야됨
#
#             else: # 내타워보다 높은거 나오면
#                 result.append(stack[-1][0]+1) # 인덱스가 아니라 ~번째임
#                 break
#
#     if not stack: # 작은애 없을 때
#         result.append(0)
#
#     stack.append([i,tower[i]]) # 현재 타워 스택에 추가 (어짜피 작으면 빠짐)
#
# for i in range(N):
#     print(result[i],end=" ")

# # AC
# # 데큐 사용 문제
# import sys
# from collections import deque
#
# for i in range(int(input())):
#     echeck=0
#     Rcount = 0
#     order=list(input())
#     orlen=int(input())
#     orlist=list(input()[1:-1].split(","))
#     Q=deque(orlist)
#
#     if orlen == 0: #덱 변환 과정에서 기본 크기 1이 생기므로 유의
#         Q = []
#
#     for j in order:
#         # print(stack)
#         if j=="R":
#             Rcount+=1 # 연속 홀수일때만 의미있음
#         elif j=="D":
#             #print("len ",len(Q))
#             if len(Q)==0: # 아무것도 없을 때 빼려고 하면
#                 print("error")
#                 echeck=1
#                 break
#             else:
#                 if Rcount%2==0 : # 안뒤집을 때( 앞에서 뽑을 때)
#                     Q.popleft()
#
#                 else: #뒤집을 때
#                     Q.pop()
#
#     if echeck == 0:
#         if Rcount % 2 == 0:  # 안뒤집을 때
#             print("[" + ",".join(Q) + "]")  # 이걸로 아래 대체 가능
#             # print("[",end="")
#             # for t in range(orlen-D-1,0,-1):
#             #     print(stack[t],end=",")
#             # print(stack[0],end="")
#             # print("]")
#
#         else:  # 뒤집을 때
#             Q.reverse()
#             print("[" + ",".join(Q) + "]")

# # AXB
# import sys
# N,K= map(int,input().split())
# print(N*K)

# # 알파벳 찾기
# import sys
# abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# result= [ -1 for i in range (26) ]
# Q=list(input())
# N=len(Q)
# for i in range(N):
#     for j in range(26):
#         if Q[i]==abc[j] and result[j]==-1:
#             result[j]=i
# for i in range(26):
#     print(result[i],end=" ")

# # 상수
# import sys
# N,K= map(str,input().split())
# N=list(N)
# K=list(K)
# N.reverse()
# K.reverse()
# N="".join(N)
# K="".join(K)
# print(max(int(N),int(K)))


# # 나머지
# import sys
# a=[]
# for i in range(10):
#     a.append(int(input())%42)
# print(len(set(a)))

# # 인공지능 시계
# import sys
#
# H,M,S = map(int,input().split())
# plus= int(input())
#
# S=S+(plus%60)
# plus=plus//60 # 분단위로 변경
# if S>=60:
#     S=S-60
#     M=M+1
# M=M+(plus%60) #시간 단위로 변경
# plus=plus//60
# if M>=60:
#     M=M-60
#     H+=1
# H=H+(plus%24)
# if H>=24:
#     H-=24
# print(H,M,S)


# # 오큰수
# import sys
# N=int(input())
# L=list(map(int,input().split()))
# result=[-1 for i in range(N)] #정답 리스트 저장
# stack=[]# 인덱스 , 값 저장
# for i in range(N):
#     while stack: #스택이 존재하는동안
#         if stack[-1][1]<L[i]: # 만약 지금까지들어온 스택에 들어온애들보다 크면 오큰수
#             a,b=stack.pop() # 인덱스 정보 받아와서
#             result[a]=L[i] # 그위치에 오큰수 넣어줌
#         else:
#             break
#     stack.append([i, L[i]]) #현재 스택보다 작은수이면 스택에 추가
#     #print(stack)
# for i in range(N):
#     print(result[i],end=" ")
#
# # 시간초과 난 코드  / 스택 사용안한 브루트 포스
# # for i in range(0,N):
# #     for j in range(i+1,N):
# #         if L[i] <L[j]:
# #             result[i]=L[j]
# #             break
# #
# # for i in range(N):
# #     print(result[i],end=" ")


# print(sum( map(int,input().split())))


# # 촌수계산
# import sys
# global check
# check=-1
# count=0
# result=[]
# def dfs(graph, v, visited,count):
#
#     visited[v] = -1
#     if v==t2:
#         result.append(count)
#
#     count += 1
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited,count)
#
# N= int(input())
# t1,t2=map(int, input().split())
# fa=[[]for i in range(N+1)]
# for i in range(int(input())):
#     a,b=map(int, input().split())
#     fa[a].append(b),fa[b].append(a)
#
# visited=[0]*(N+1)
# dfs(fa, t1, visited, count)
# if not result:
#     print(-1)
# else:
#     print(result[0])


# #큐
# import sys
# input=sys.stdin.readline
# from collections import deque
# Q=[]
# Q=deque(Q)
# for i in range(int(input())):
#     P=input().split()
#     LP=len(P)
#     if LP==2:
#         P[1]=int(P[1])
#     #print(P)
#     if P[0]=="push":
#         Q.append(P[1])
#     elif P[0]=="pop":
#         if Q:
#             print(Q.popleft())
#         else:
#             print(-1)
#     elif P[0]=="size":
#         print(len(Q))
#     elif P[0]=="empty":
#         if Q:
#             print(0)
#         else:
#             print(1)
#     elif P[0] == "front":
#         if Q:
#             print(Q[0])
#         else:
#             print(-1)
#
#     else:
#         if Q:
#             print(Q[-1])
#         else:
#             print(-1)
#     P.clear()

# #리모컨
# import sys
# input=sys.stdin.readline
# #모든 버튼이 고장났을때 / 모든 버튼이 멀정할 때 / 입력받은게 100일때
# #-> 브루트 포스 풀이 시 위의 사항 고려안해도 모든 경우를 고려하기 때문에 그에맞게 코딩하면 됨
# #점프하고 올라가거나 내려갈때는 점프( 자리수 만큼 번호사용 : len)
#
# N = int(input()) #이동채널
# M = int(input()) #고장난채널수
# B=[]
# if M != 0:
#     B = list(map(int, input().split()))  # 고장 버튼 모음
#
# #단순 터치이동 - 일단 결과로 저장
# result = abs(N - 100)
# #직접이동 = 이동한 순간의 이동횟수 + 거기서 목표채널까지 이동하는 숫자
# for i in range(0,1000001):  # 100만이상은 아래에서 올라가는게 빠름
#     stri = str(i)#  길이 체크
#     for j in range(len(stri)):  # 문자열로 바꿔서 첫째자리부터 확인 (문자열 반복가능)
#         if int(stri[j]) in B :# 고장난 채널이 사용되면
#             break
#         if (len(stri)-1)== j:# 마지막 자리까지 오면
#             result= min(result   , abs(N-i) + len(stri)) #아까 최소 아님, 현재i에서 가는 최소
# print(result)


# # 줄번호
# # import sys
# # input=sys.stdin.readline
# for i in range(int(input())):
#     print((str(i+1))+".",input())


# # 세수정렬
# a=list(map(int,input().split()))
# a.sort()
# for i in range(len(a)):
#     print(a[i],end=" ")

# # 최댓값
# a=[]
# for i in range(0,9):
#    a.append([int(input()),i+1])
# a.sort(reverse=True)
# # print("a",a)
# print(a[0][0])
# print(a[0][1])



# # 프린터 큐
# import sys
# input=sys.stdin.readline
# for i in range(int(input())):
#     result=0
#     N,M = map(int,input().split())
#     L2 = [0 for i in range(N)]
#     L=list(map(int,input().split(" ")))
#     result=0
#     while M!=-1:
#         if L[0] == max(L):
#             L.pop(0)
#             M-=1
#             result+=1
#         else:
#             L.append(L[0])
#             L.pop(0)
#             if M==0:
#                 M=len(L)-1
#             else:
#                 M-=1
#     print(result)

# #문자열 반복
# import sys
# input=sys.stdin.readline
# count1=0
# count2=0
# l=list(map(int,input().split()))
# for i in range(0, 8):
#     if l[i] == i + 1:
#         count1 += 1
# for i in range(0, 8):
#     if l[i] == 8-i:
#         count2 += 1
# if count1 == 8:
#     print("ascending")
# elif count2 == 8:
#     print("descending")
# else:
#     print("mixed")



# # OX 퀴즈
# import sys
# #input=sys.stdin.readline
# for k in range(int(input())):
#     result=0
#     p=1
#     l=list(input())
#     l.insert(0,"X")
#     for i in range(1,len(l)):
#         if l[i]=="O":
#             if l[i-1]=="X":
#                 p=1
#                 result+=p
#             else :
#                 p+=1
#                 result+=p
#     print(result)


# # 숫자의 합
# import sys
# #input=sys.stdin.readline
# n=int(input())
# l=list(map(int,input()))
# print(sum(l))

# # A/B
# import sys
# #input=sys.stdin.readline
# a,b=map(int,input().split())
# print(a/b)

# # 알고리즘 수업 - 깊이 우선 탐색 1
# import sys
# input=sys.stdin.readline
# sys.setrecursionlimit(10**9)
# count=1
# N,M,R=map(int, input().split())
#
# visited=[0]*(N+1)
# visited[0]=-1
#
# path=[]
# result=[0]*(N+1)
# fa=[[]for i in range(N+1)]
#
# for i in range(M):
#     a,b=map(int, input().split())
#     fa[a].append(b),fa[b].append(a)
#
# for i in range(1,N+1):
#     fa[i].sort()
#
# def dfs(v):
#     visited[v] = 1
#     path.append(v)
#     for i in fa[v]:
#         if not visited[i]:
#             dfs(i)
# dfs(R)
#
# for idx, node in zip(range(1, len(path)+1), path):
#     result[node] = idx
#
# #print (result)
# for i in range (1,N+1):
#     print(result[i])

#
# # 알고리즘 수업 - 너비 우선 탐색 1
# from collections import deque
# import sys
# input=sys.stdin.readline
# sys.setrecursionlimit(10**9)
# count=1
# N,M,R=map(int, input().split())
#
# visited=[0]*(N+1)
# visited[0]=-1
#
# path=[]
# result=[0]*(N+1)
# fa=[[]for i in range(N+1)]
#
# for i in range(M):
#     a,b=map(int, input().split())
#     fa[a].append(b),fa[b].append(a)
#
# for i in range(1,N+1):
#     fa[i].sort()
#
# def dfs(v):
#     visited[v] = 1
#     print(v,end=" ")
#     for i in fa[v]:
#         if not visited[i]:
#             dfs(i)
#
# def bfs(graph,v,visited):
#     Q=deque([v])
#     visited[v]=-1
#     while Q:
#         v=Q.popleft()
#         path.append(v)
#         #print(v)
#         for i in graph[v]:
#             if not visited[i]:
#                 Q.append(i)
#                 visited[i]=-1
#
#
# bfs(fa,R,visited)
#
# for idx, node in zip(range(1, len(path)+1), path):
#     result[node] = idx
#
# #print (result)
# for i in range (1,N+1):
#     print(result[i])


# # DFS 와 BFS
# from collections import deque
# import sys
# input=sys.stdin.readline
# sys.setrecursionlimit(10**9)
# count=1
# N,M,R=map(int, input().split())
#
# visited=[0]*(N+1)
# path=[]
# result=[0]*(N+1)
# fa=[[]for i in range(N+1)]
#
# for i in range(M):
#     a,b=map(int, input().split())
#     fa[a].append(b),fa[b].append(a)
#
# for i in range(1,N+1):
#     fa[i].sort()
#
# def dfs(v):
#     visited[v] = 1
#     print(v,end=" ")
#     for i in fa[v]:
#         if not visited[i]:
#             dfs(i)
#
# def bfs(graph,v,visited):
#     Q=deque([v])
#     visited[v]=-1
#     while Q:
#         v=Q.popleft()
#         #path.append(v)
#         print(v,end=" ")
#         for i in graph[v]:
#             if not visited[i]:
#                 Q.append(i)
#                 visited[i]=-1
#
# dfs(R)
# print("")
# visited=[0]*(N+1)
#
# bfs(fa,R,visited)
#
# # for idx, node in zip(range(1, len(path)+1), path):
# #     result[node] = idx
# # #print (result)
# # for i in range (1,N+1):
# #     print(result[i])

