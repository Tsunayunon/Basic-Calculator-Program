a= int(input("Birinci sayıyı giriniz: "))
c= input("Yapmak istediğiniz işlemi giriniz: ")
b= int(input("İkinci sayıyı giriniz: "))
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
elif c=="**":
    print(a**b)
else:
    print("Yanlış işlem girdiniz!")