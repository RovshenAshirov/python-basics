n = int(input("List elementlari sonini kiriting: "))
a = []

for i in range(n):
    a.append(input(f"{i}-elementni kiriting: "))

maxi = a[0]
mini = a[0]

for i in range(n):
    if maxi < a[i]:
        maxi = a[i]
    if mini > a[i]:
        mini = a[i]

m = 0 
k = 0

for i in range(n):
    if maxi == mini:
        n = 0
        break
    if maxi == a[i]:
        m = m + 1
    if mini == a[i]:
        k = k + 1

print(n-(m+k))