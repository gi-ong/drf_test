# x = int(input())
# i = 1

# while i <= x:
#     print(i,i*i)
#     i += 1

# a = 100
# i = 1

# while i < 11:
#     a = a * 3 / 5
#     print(i, round(a, 4))
#     i += 1


# n = 358
# rem = rev = 0
# while n >= 1:
#     rem = n % 10
#     rev = rev * 10 + rem
#     n = n // 10

# print(rev)

# print(n % 10) #8
# print(n // 10) #35


##

# x = int(input())
# r = str(x)

# if x >= 1000000:
#     r = str(x // 1000000) + 'M'
# else:
#     pass

# print(r)

######

# s = 0

# while True:
#     n = int(input())
#     if n < 0:
#         break
#     else:
#         s += n

# print(s)


#######


# l = ['1','1','1','1','1','1','1','2']

# def split_l(a):
#     half = len(a)//2
#     return a[:half], a[half:]
# l = [1,1,1,1,1,1,1,2]
# a, b = split_l(l)

# ax,ay = split_l(a)
# bx,by = split_l(b)

# def diff():
#     where(ax,bx)
#     return


# def where(a,b):
#     if sum(a) == sum(b):
#         diff()
#         return print('같음') 
#     else:
#         diff()
#         return print('다름')



# where(ax,ay)

##############

# a = int(input("입력하세요: "))

# for i in range(1,1+a):
#     print(a)

##########

# num = int(input())

# for i in range(1, num+1):
#     print(i, i*i)


######

# num = input().split()
# min = int(num[0])
# num.reverse()
# max = int(num[0])

# temp = int(input())

# while temp != -999:
#     if min <= temp <= max:
#         print('Nothing to report')
#         temp = int(input())
#     else:
#         print('Alert')
#         break

########

#python 3.10 이후

# for n in range(1,11):
#     match n % 2:
#         case 0:
#             print(f"{n} is even")
#         case 1:
#             print(f"{n} is odd")

#############

# for x in range(4):
#     print(x)
# else:
#     print("리스트 원소 모두 출력 완료")

# countdown = 5

# while countdown > 0:
#     print(countdown)
#     countdown -= 1
#     if input() == '중단':
#         break
# else:
#     print('발사')
    
######################

# def what(a,b):
#     if a == b:
#         print(a,' = ',b)
#     elif a > b:
#         print(a,' > ',b)
#     else:
#         print(a,' < ',b)
        
# what(1,100)

# from turtle import *
# shape('turtle')

##############

# for i in range(2,10):
#     print(i,'단 시작')
#     for j in range(1,10):
#         print(i, ' * ', j, ' = ', i*j)
#     else:
#         print(i,'단 끝')
# else:
#     print('구구단 끝')
    
    
def base62(index):
    result = ""
    index = len(index)
    words = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    while index % 62 > 0 or result == "":
        result = result + words[index % 62]
        index = int(index / 62)
    return result


def generate(url):
    # index = DB.insert(url)
    short = base62(url)
    print(short)
    return short

generate("http://gdaj.net/go/?utm_source=naver&utm_medium=blog&utm_campaign=reserve&utm_id=go")