# string = 'пара-ра-рам рам-пам-папам па-ра-па-да'
str = input()
array = str.split()
count = array[0].count('а')
for i in range(len(array)):
     if array[i].count('а') == count:
         continue
     else:
         print("Gам парам")
         break
else:
    print("Парам пам-пам")