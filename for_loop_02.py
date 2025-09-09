# '''
# Napisite program koji ispisuje trokut tako da su linije stranica prikazane zvjezdicama *.

# *
# **
# * *
# *  *
# *   *
# *    *
# *******
# '''
# print('Ispis trokuta fiksne visine bez for petlje')
# print('*')
# print('**')
# print('* *')
# print('*  *')
# print('*   *')
# print('*    *')
# print('*******')
# print()
# print()









# print('Ispis trokuta fiksne visine pomocu for petlje')
# print('*')

# for number in range(5):
#     print('*' + ' ' * number + '*')

# print('*******')
# print()
# print()












# print('Ispis trokuta varijabilne visine pomocu for petlje')

# height = int(input('Unesite visinu trokuta: '))

# print('*')
# for number in range(height - 2):
#     # print('*' + ' ' * number + '*')
#     print(f'*{" " * number}*')

# # print('*' + '*' * (height - 2) + '*')
# print(f'{"*" * height}')
# print()
# print()















# print('Ispis trokuta varijabilne visine pomocu for petlje')
# print('uz izbor znaka za iscrtavanje linija strnica trokuta')

# height = int(input('Unesite visinu trokuta: '))
# symbol = input('Unesite znak za iscrtavanje stranica trokuta: ')

# print(symbol)
# for number in range(height - 2):
#     print(f'{symbol}{" " * number}{symbol}')

# print(f'{symbol * height}')
# print()
# print()













# Pitanje 
# Vladimir Stipetić: zašto moram staviti u zagradu x + 0?

z = input('znak za ispis stranica trokuta: ')
x = int(input('visina stranice trokuta: '))

print(z)
for number in range(x - 2):
    print(z + ' ' * number + z)
print(z * x + 0) # ne radi jer nije moguce povezivati (+)  niti oduzimati (-) str i int tipove podataka
print(z * x + '0')