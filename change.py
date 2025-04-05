def change():
    expense = 23.75
    money = 100
    Vuelto = (money - expense)
    Pesos = int(Vuelto)
    Cents = int(round((Vuelto - Pesos) * 100))
    print(f"Ingresar gasto:\n{expense}\nDinero recibido\n{money}\n\nVuelto\n\nPesos:\n{Pesos}\nCentavos:\n{Cents}")

