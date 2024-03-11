edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("Ingresa una edad valida.")
elif edad < 12:
    print("Eres un niño")
elif edad < 18:
    print("Eres un adolescente")
elif edad < 65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor.")