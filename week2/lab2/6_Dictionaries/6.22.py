thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(x)                  #1way
  
for x in thisdict:
    print(thisdict[x])        #2way
    
for x in thisdict.values():
    print(x)                  #3way