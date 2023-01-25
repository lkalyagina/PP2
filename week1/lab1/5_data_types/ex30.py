dictionary = {"name" : "John", "age" : 36}
print(type(dictionary)) 

set1 = {"apple", "banana", "cherry"}
print(type(set1)) 

frozen = frozenset({"apple", "banana", "cherry"})
print(type(frozen)) 

e = True
print(type(e)) 

f = b"Hello"
print(type(f)) 

g = bytearray(5)
print(type(g))

h = memoryview(bytes(5))
print(type(h))

i = None
print(type(i))  