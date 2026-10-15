print("----------Una simple calculadora de Python----------\n")

def suma(x, y):
   return x + y

def resta(x, y):
   return x - y

def multiplicar(x, y):
   return x * y

def dividir(x, y):
   return x / y

print("Seleccione una operación.\n")
print("1.Suma")
print("2.Resta")
print("3.Multiplicación")
print("4.División")

choice = input("\nIngrese una opción (1/2/3/4):")

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", suma(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", resta(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiplicar(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", dividir(num1,num2))
else:
   print("Invalid input")
