#📘 Iterators
#An iterator is an object that allows you to traverse through elements one at a time.
#It implements two methods:
#__iter__() → returns the iterator object itself.
#__next__() → returns the next value, raises StopIteration when no items left.
#Example: Iterator

# List is iterable
nums = [1, 2, 3]
it = iter(nums)   # get iterator

print(next(it))   # 1
print(next(it))   # 2
print(next(it))   # 3
# next(it) → StopIteration
#👉 Iterators give elements one by one until exhausted.

#📘 Generators
#A generator is a simpler way to create iterators using the yield keyword.
#Functions with yield return a generator object.
#They generate values on the fly (lazy evaluation), saving memory.
#Example: Generator Function

def my_gen():
    yield 1
    yield 2
    yield 3

g = my_gen()
print(next(g))   # 1
print(next(g))   # 2
print(next(g))   # 3

#📘 Generator Expressions
#Similar to list comprehensions, but with () instead of [].
#More memory-efficient.

gen = (x*x for x in range(5))
for val in gen:
    print(val)