# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# name = 'Rego'
# print(name)
# print(type(name))
#
# name2="Zolika"
#
# print((name+' '+name2)*6)
# print (6)
#
# eletkorom = 36
# print(eletkorom)
# print(eletkorom/6)
# nev=input("Add meg a neved:")
# print('Szia' + ' ' + nev + '!')
# age=33
# eletkorom = age
# print(eletkorom)
name=input("Írd be a neved! ")
age = int(input("Hány éves vagy? "))
if age > 18:
    print("Nagykorú vagy!")
    if age>60:
        print("Sőt öreg vagy már...")
    if name == "Regő":
        print("Jól megy a kódolás"+" "+ name+ "!")
else:
    print("Fiatal vagy még!")
