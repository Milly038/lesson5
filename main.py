# loops - for

fruits = ["apple", "banana", "strawberry"]

for fruit in fruits:
    print(fruit)

fjala = "Kimik"

for shkronje in fjala:
    print(shkronje)

# in range

# for number in range(1,11):
#     if number == 5:
#         continue
#     print(number)

lista = [1,2,3,4,5,6,7,8,9]

total_sum = 0

for num in lista:
    if num %2 ==0:
        total_sum = total_sum + num

print("Shuma totale e numrave cift eshte: ",total_sum)
