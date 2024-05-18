# How to Deep Copy a List
# Qanday qilib ro'yxatni chuqur nusxalaymiz

my_favorite_things = ["Working out", 7, ["amazon prime", "netflix"]]
copy = my_favorite_things.copy()

print(my_favorite_things, copy)

copy[2][0] = "hulu"

print(my_favorite_things, copy)
print(id(my_favorite_things[2]), id(copy[2]))

# -----------------------------------
import copy

my_favorite_things = ["Working out", 7, ["amazon prime", "netflix"]]

c = copy.deepcopy(my_favorite_things)

print(my_favorite_things, c)

c[2][0] = "hulu"

print(my_favorite_things, c)
print(id(my_favorite_things[2]), id(c[2]))


