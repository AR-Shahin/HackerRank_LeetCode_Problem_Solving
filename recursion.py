

# def namta(n):
#     if n == 0:
#         return
#     else:
#         for i in range(1, 11):
#             print("{} * {} = {}".format(i, n, i*n))
#         if n != 1:
#             print('-----------------------')
#         namta(n-1)

def print_namta(n, m):
    if m == 0:
        return
    else:
        print("{} * {} = {}".format(m, n, m*n))
        print_namta(n, m-1)


def namta(n, m):
    if n == 0:
        return
    else:
        print_namta(n, m)
        if n != 1:
            print('-----------------------')
        namta(n-1, m)


n = 3
m = 12
namta(n, m)
