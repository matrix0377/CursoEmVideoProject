# exercício com listas

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.insert(2, 0) # posição, elemento
num.sort(reverse=True)

if 5 in num:
    num.remove(5)
    
print(num)
print(f'Essa lista tem {len(num)} elementos.')
