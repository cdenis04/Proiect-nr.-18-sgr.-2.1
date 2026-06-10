from proiect import Student, Profesor, Echipament, Laborator
if __name__ == "__main__":
    student1 = Student(nume="Ciobanu Razvan", email="razvan.ciobanu@student.upt.ro", grupa="2.1")
    profesor1 = Profesor(nume="Rares Nicolae", email="rares.nicolae@upt.ro", departament="Electronica")

    e1 = Echipament(nume="Osciloscop Digital", cod_inventar="OSC-001")
    e2 = Echipament(nume="Multimetru Fluke", cod_inventar="MULT-102")
    e3 = Echipament(nume="Sursa Tensiune", cod_inventar="SUR-04", stare="Defect")
    e4 = Echipament(nume="Multimetru UNI-T", cod_inventar="MULT-105")