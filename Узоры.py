#Узор снежинка
# from turtle import *
# ht()
# pensize(2)
# colormode(255)
# for r in range(40, 0, -10):
#     for i in range(6):
#         color(255, 165, r * 6)
#         fillcolor(162, r * 6, 255)
#         begin_fill()
#
#         left(60)
#         for _ in range(4):
#             forward(r)
#             left(90)
#         end_fill()
# done()

#Узор снежинка2

from turtle import *
ht()
pensize(2)
colormode(255)
for r in range(40, 0, -10):
    for i in range(6):
        color(255, 165, r * 6)
        fillcolor(162, r * 6, 255)
        begin_fill()
        left(60)
        for _ in range(3):

            forward(r)
            left(120)
        end_fill()
done()