# Creati un repository temacurs16. 

# Scrieti un program de gestiune a angajatilor.
# Acesta trebuie sa retina pentru fiecare angajat numele prenumele si salariul intr-un fisier (alegeti voi daca txt csv sau json). 
# Programul trebuie sa permita: 
# 1.introducerea unui angajat nou (adauga datele angajatului in fisier - datele sunt citite de la tastatura)
# 2.stergerea unui angajat pe baza numelui. Angajatul este sters din fisier. 
# 3.afisare toti angajatii. 
# 4.Pentru ca urilizatorul sa selecteze ce vrea sa faca ii vom crea la final un meniu ( sa aleaga 1 ptistare angajati, 2 pt adaugare etc) 

# Pentru fiecare punct de mai sus( fiecare feature) creati un branch nou (numele branchului sa fie sugestiv referitor la feature-ul pe care 
#il implementat),  si apoi faceti pull request catre master. 



import json
import os

datafile = "listaTrantori.json"


def trantori_management_extraordinaire():
    action = None
    options = {"angajare": "A", "concediere": "C", "listare": "L", "iesire": "X"}
    while not action == options["iesire"]:
        action = input(f"Ce facem astazi, sefu?\n {options['angajare']} - Angajam, {options['concediere']} - Concediem, {options['listare']} - Ne uitam la lista, {options['iesire']} - Inchidem?").upper()
        if action == options["angajare"]:
            hireTrantor()
        elif action == options["concediere"]:
            fireTrantor()
        elif action == options["listare"]:
            printAllTrantori()
        elif action == options["iesire"]:
            break
        else:
            print("Sefu, se pare ca nu sunteti atent. Nu-i nimic, incercam inca odata.\n")



def saveTrantorData(outputPath, entry):
    listOfTrantori = readTrantorData(outputPath)
    listOfTrantori.append(entry)
    file = open(outputPath, "w")
    file.write(json.dumps(listOfTrantori))
    file.close()



def removeTrantorData(outputPath, entry):
    listOfTrantori = readTrantorData(outputPath)
    for x in listOfTrantori:
        if x["name"] == entry:
            listOfTrantori.remove(x)
            break
    with open(outputPath, "w") as file:
        file.write(json.dumps(listOfTrantori))



def readTrantorData(inputPath) -> list:
    result = []
    if os.path.exists(inputPath):
        file = open(inputPath, "r")
        content = file.read()
        if len(content) != 0:
            trantori = json.loads(content)
            for x in trantori:
                result.append(x)
        file.close()
    return result



def hireTrantor():
    output = datafile
    name = input("Cum il cheama? ").capitalize()
    family = input("Numele de familie? ").capitalize()
    salary = input("Cat vrea? ")

    saveTrantorData(output, {"name": name + " " + family, "salary": salary})
    


def fireTrantor():
    file = datafile
    name = input("cum il cheama? ").capitalize()
    family = input("Numele de familie? ").capitalize()

    removeTrantorData(file, (name + " " + family))

    print(f"Gata. L-am dat afara pe {name} {family}. Pacat. Era om de treaba")



def printAllTrantori():
    listOfTrantors = readTrantorData(datafile)
    for trantor in listOfTrantors:
        print(f"{trantor['name']}{24 * '.'}{trantor['salary']}" )
        print(48*"-")



#run the damned thing
trantori_management_extraordinaire()