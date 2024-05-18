# Strings are Immutable
# Satrlar o'zgarmasdir

task = "Subscribe"
different = task

print(id(task))

different = "hey"

print(task)
print(id(different))
