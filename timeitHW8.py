import timeit

t = timeit.Timer('HW6p2','import HW6p2')
print("CPU Compute: " , t.timeit(number=100))
t2 = timeit.Timer('HW8','import HW8')
print("Parallel Compute: " , t2.timeit(number=100))
print("Parallel/CPU Percent faster: ", ((t2.timeit(number=100)/t.timeit(number=100))-1)*100)
