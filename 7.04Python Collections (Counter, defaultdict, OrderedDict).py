#1. 🔢 Counter
#A dictionary subclass designed for counting hashable objects.
#Stores elements as keys and their counts as values.

#✅ Example

from collections import Counter

# Count frequency of elements in a list
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = Counter(fruits)

print(count)          # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})
print(count["apple"]) # Output: 3
print(count.most_common(2))  # Output: [('apple', 3), ('banana', 2)]

#2. 📂 defaultdict
#A dictionary subclass that provides a default value for missing keys.
#Prevents KeyError by automatically initializing the key with a default factory (like int, list, set).

#✅ Example:


from collections import defaultdict

# Group words by their first letter
words = ["apple", "banana", "cherry", "avocado"]
grouped = defaultdict(list)

for word in words:
    grouped[word[0]].append(word)

print(grouped)

# Output: defaultdict(<class 'list'>, {'a': ['apple', 'avocado'], 'b': ['banana'], 'c': ['cherry']})

#3. 📜 OrderedDict
#A dictionary subclass that remembers the insertion order of keys.
#In Python 3.7+, normal dictionaries also preserve insertion order, but OrderedDict adds extra methods like move_to_end.

#✅ Example:

from collections import OrderedDict

# Maintain insertion order
ordered = OrderedDict()
ordered["a"] = 1
ordered["b"] = 2
ordered["c"] = 3

print(ordered)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Move key 'a' to the end
ordered.move_to_end("a")
print(ordered)  # Output: OrderedDict([('b', 2), ('c', 3), ('a', 1)])