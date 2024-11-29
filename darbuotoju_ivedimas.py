darbuotoju_sarasas = []

while True:
    print("""pasirinkite "1" - ivesti darbuotoja
pasirinkite "2" - perziureti darbuotoju sarasa
pasirinkite "q" - ivestis baigta
""")
    ivestis = input(" > ")
    if ivestis == "q":
        break
    if ivestis == "1":
        vardas = input("Iveskite darbuotojo varda: ")
        pareigos = input("Iveskite darbuotojo pareigas: ")
        atlyginimas = input("Iveskite darbuotojo atlyginima: ")
        darbuotojas = [vardas, pareigos, atlyginimas]
        darbuotoju_sarasas.append(darbuotojas)
    elif ivestis == "2":
        for darbuotojas in darbuotoju_sarasas:
            print(darbuotojas)
