a=int(input())
b=int(input())
c=int(input())
d= b*b - 4*a*c
if d > 0:
    otv1= (-b + d**(0.5))/(2 * a)
    otv2= (-b - d**(0.5))/(2 * a)
    print( otv1, otv2)
elif d == 0 :
    otv=-b / 2 * a
    print(otv)
else:
    print("корней нет")