# Задание 2.1

a = 2020


def is_year_leap(a):
    if a % 4 == 0:
       b = True
    else:
        b = False
    return b


if is_year_leap(a):
    print('Год', a, "высокосный")
else:
    print('Год', a, "не высокосный")

# Задание 2.2

a = 22
b = 34
c = 64


def triangle(a, b, c):
    if (a + b > c) and (b + c > a) and (a + c > b):
        k = True
    else:
        k = False
    return k


if triangle(a, b, c):
    print("Треугольник с такими сторонами {0} {1} {2} существует ".format(a, b, c))
else:
    print("Треугольника с такими сторонами {0} {1} {2} не существует ".format(a, b, c))

# Задание 2.3

a = 39
b = 58
c = 1


def triangleee(a, b, c):
    if (a + b > c) and (b + c > a) and (a + c > b):
        if a == b == c:
            reply = "Equilateral triangle"
        elif (a == b) or (a == c) or (b == c):
            reply = "Isosceles triangle"
        else:
            reply = 'Versatile triangle'
    else:
        reply = "Not a triangle"
    return reply


s = triangleee(a, b, c)
print(s)

# Задание 2.4
x1 = 10
y1 = 8
x2 = 12
y2 = 7


def distance(a, b):
    reply = a - b
    return reply


response1 = distance(x1, y1)
response2 = distance(x2, y2)
print("Растояние между {0} и {1} ровно {2} \nРастояние между {3} и {4} ровно {5}".format(x1, y1, response1, x2, y2, response2))
