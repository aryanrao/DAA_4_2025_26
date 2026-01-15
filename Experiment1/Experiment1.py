import time
global operations, depth, n_list

depth = 0
n_list = []
operations = 0

def complexRec(n):
    global operations, depth, n_list
    if n not in n_list:
        depth +=1
        n_list.append(n)
    else:
        pass

    if n <= 2:
        return

    p = n
    while p > 0:
        temp = [0] * n
        operations +=n
        for i in range(n):
            temp[i] = i ^ p
            operations+=1
        p >>= 1
        operations+=1

    small = [0] * n
    operations+=n
    for i in range(n):
        small[i] = i * i
        operations+=1

    if n % 3 == 0:
        small.reverse()
        operations+=n
    else:
        small.reverse()
        operations+=n

    complexRec(n // 2)
    complexRec(n // 2)
    complexRec(n // 2)


start = time.time()
complexRec(128)
end = time.time()

time_taken = (end-start)*1000
print(f"Time Taken: {time_taken} ms")
print(f"No of Operations: {operations}")
print(f"Depth: {depth}")
