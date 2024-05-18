# How to Copy a List
# Ro'yxatni qanday qilib nusxalaymiz

my_favorite_things = ["Working out", 7, ["amazon prime", "netflix"]]
print(id(my_favorite_things))

print(my_favorite_things[1:2])

copy = my_favorite_things  # nocopy
print(id(copy))

copy = my_favorite_things[:]
print(id(copy))

copy = my_favorite_things.copy()
print(id(copy))

copy[0] = "Walking"
print(my_favorite_things, copy)
