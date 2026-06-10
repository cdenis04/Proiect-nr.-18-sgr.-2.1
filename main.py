from proiect import Student, Profesor, Echipament, Laborator
if __name__ == "__main__":
    student1 = Student(nume="Ciobanu Razvan", email="razvan.ciobanu@student.upt.ro", grupa="2.1")
    profesor1 = Profesor(nume="Rares Nicolae", email="rares.nicolae@upt.ro", departament="Electronica")

    e1 = Echipament(nume="Osciloscop Digital", cod_inventar="OSC-001")
    e2 = Echipament(nume="Multimetru Fluke", cod_inventar="MULT-102")
    e3 = Echipament(nume="Sursa Tensiune", cod_inventar="SUR-04", stare="Defect")
    e4 = Echipament(nume="Multimetru UNI-T", cod_inventar="MULT-105")

    lab= Laborator("Sisteme Electronice")
    lab.adauga_echipament(e1)
    lab.adauga_echipament(e2)
    lab.adauga_echipament(e3)
    lab.adauga_echipament(e4)

    print("\n--- Inainte de sortare ---")
    lab.afiseaza_toate_echipamentele()
    lab.sorteaza_echipamente()
    print("\n--- Dupa sortare alfabetica ---")
    lab.afiseaza_toate_echipamentele()
    print("\n--- Rezultate cautare: 'Multimetru Fluke' ---'")
    rezultate = lab.cauta_echipament("Multimetru Fluke")
    for r in rezultate:
        r.afiseaza_echipament()

    print("\n--- Sesiune de imprumuturi ---")
    imprumut1 = lab.imprumuta_echipament("OSC-001",student1)

    lab.imprumuta_echipament("OSC-001",profesor1)
    lab.imprumuta_echipament("SUR-04",profesor1)
    lab.imprumuta_echipament("ID_GRESIT",student1)
    print("\n--- Returnare ---")

    if imprumut1:
        imprumut1.returneaza_echipament()

    lab.raport_defecte_csv()