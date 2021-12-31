def solution(n):
    if n % 2 != 0:
        print("Weird")
        return
    elif n >= 2 and n <= 5:
        print("Not Weird")
        return
    elif n >= 6 and n <= 20:
        print("Weird")
        return
    else:
        print("Not Weird")
        return


if __name__ == '__main__':
    solution(18)


n = int(input().strip())
check = {True: "Not Weird", False: "Weird"}

print(check[
    n % 2 == 0 and (
        n in range(2, 6) or
        n > 20)
])
