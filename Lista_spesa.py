listaSpesa = []

#AGGIUNTA PRODOTTO
def Addproduct():
    inp1 = input("Aggiungi un prodotto: ")
    listaSpesa.append(inp1)

#VISUALIZZA PRODOTTO
def Viewproduct():
    print("LISTA DELLA SPESA:")
    index = 0
    for i in listaSpesa:    
        print(f"{index}) {i}")
        index = index + 1
    if len(listaSpesa) == 0:
        print("LISTA DELLA SPESA VUOTA!")

#RIMUOVI PRODOTTO
def Removeproduct():
    Viewproduct()
    inp1 = int(input("Inserisci l'ID del prodotto che vuoi rimuovere: "))
    listaSpesa.pop(inp1)

#CONTA I PRODOTTI
def Countproduct():
    print("NUMERO PRODOTTI:")
    print(len(listaSpesa))

#SVUOTA LA LISTA    
def Clearproduct():
    listaSpesa.clear()

while True:
    print("""
    1) AGGIUNGI PRODOTTO
    2) VISUALIZZA PRODOTTO
    3) RIMUOVI PRODOTTO
    4) CONTA I PRODOTTI
    5) SVUOTA LA LISTA
    6) ESCI
    """)
    Opzinp = int(input(""))
    if Opzinp == 1:
        Addproduct()
    elif Opzinp == 2:
        Viewproduct()
    elif Opzinp == 3:
        Removeproduct()
    elif Opzinp == 4:
        Countproduct()
    elif Opzinp == 5:
        Clearproduct()
    elif Opzinp == 6:
        break

