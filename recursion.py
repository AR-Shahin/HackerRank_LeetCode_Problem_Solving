

# def print_namta(n):
#     temp = 1
#     if temp == 0:
#         return
#     else:
#         print("{} * {} = {}".format(temp, n, temp*n))
#         temp += 1
#         print_namta
#     for i in range(1, 11):
#         print("{} * {} = {}".format(i, n, i*n))

def namta(n):
    if n == 0:
        return
    else:
        for i in range(1, 11):
            print("{} * {} = {}".format(i, n, i*n))
        if n != 1:
            print('-----------------------')
        namta(n-1)


n = 12
namta(n)
