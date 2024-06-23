import timeit

#LIST SPEED TEST
print(timeit.timeit(stmt='["red", "blue", "green", 5, 7, 12, 18, "dude"]', number=10000000))

#TUPLE SPEED TEST
print(timeit.timeit(stmt='("red", "blue", "green", 5, 7, 12, 18, "dude")', number=10000000))
