# def emriFunksionit(parametri1, parametri2):
# print("Hello funksion")

def helloworld():
    print("Hello World")

helloworld()

def mbledhja(a,b):
    rezultati = a + b

    return rezultati

print(mbledhja(3,5))

def prezentimi(name):
    return f"Pershendetje per {name}"

print(prezentimi("Qamilin"))

def numriMeIMadh(lista):

    largest_num = 0

    for num in lista:
        if num > largest_num:
            largest_num = num

    return largest_num

lista = [123,4,244,12,1442]

print(numriMeIMadh(lista))



# default arguments

def emri_mbiemri(emri, mbiemri="Berisha"):
    return f"Hello {emri} {mbiemri}"

print(emri_mbiemri("Besart"))