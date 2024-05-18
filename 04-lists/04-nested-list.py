# Intro to Nested List
# Ichma-ich ro'yxatga kirish

my_favorite_things = ["Working out", 7, ["amazon prime", "netflix"]]
print(my_favorite_things[2])

my_favorite_things = ["Working out", 7, ["amazon prime", ["netflix", "hulu"]]]
print(my_favorite_things[2][1][0])
print(len(my_favorite_things[2][1]))
