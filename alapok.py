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
