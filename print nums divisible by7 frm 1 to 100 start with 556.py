# i=556
# while i<=666:
#     z=i-555
#     if z*7<=100:
#         print(z*7)
#     i=i+1
#without using modulus operator

i=556
while i<=666:
    z=i-555
    if z%7==0 and z<=100:
        print(z)
    i=i+1
#by using modulus

    