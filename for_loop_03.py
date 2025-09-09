# range(10) generira raspon od 0 do 9
print()

for number in range(10):
    print(number, end=' ')

print()
print()



# Napisiste kod koji ispisuje brojeve od 10 do 0

# Kada je korak pozitivan broj generiranje brojeva u rasponu je s lijeva na desno odnosno od manjeg prema vecem
# Kada je korak negativan broj generiranje brojeva u rasponu je s desna na lijevo odnosno od veceg prema manjem
#              start, stop, step
for number in range(10, -1, -1):
    print(number, end=' ')

print()
