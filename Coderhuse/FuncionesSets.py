set1 = {1, 2, 3, 4}
set2 = set1.copy() # copia el set a la nueva variable 
print(set2)
set1 = {1,2,3,4}
set2 = {5,6,7,9}

print(set1.isdisjoint(set2))
