unique = {1,0,2,0,3,2,4,2,1}
print(f"set prevent duplicate elements example unique: {unique} and {type(unique)} and length : {len(unique)}")

#no positional indexing in sets
print("="*10)
a = {1,2}
a.add(3)
print(f"set a = {a}")
print("="*20)
# a.remove(20) #KeyError: 20
# print(f"set a : {a}")
a.discard(30)  #okay if absent
print(f"Set a = {a}")
# set uses in (membership) to searching  true elements
print(f"3 in set a {a} : {3 in a}")
print("="*20)#hashable types and set restrictions
# a = {[1,2],[2,3]} #TypeError: unhashable type: 'list'
# a = {([1,2],3),(11)}#TypeError: unhashable type: 'list' #tuple contents are list
a = {(1,2),(2,1)}
print(a)

