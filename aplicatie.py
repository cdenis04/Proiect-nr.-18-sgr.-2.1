import tkinter as tk
from tkinter import messagebox
from clase import Student, Echipament, Laborator


class InterfataLaborator:
    def __init__(self, root, laborator):
        self.lab = laborator
        self.root = root
        self.root.title(f"Gestiune - {self.lab.nume}")
        self.root.geometry("450x400")

        tk.Label(root, text="Echipamente în Laborator", font=("Helvetica", 14, "bold")).pack(pady=10)
        self.lista_echipamente = tk.Listbox(root, width=50, height=10)
        self.lista_echipamente.pack(pady=5)

        tk.Button(root, text="Actualizează Lista", command=self.incarca_date).pack(pady=5)

        tk.Label(root, text="Introdu Codul de Inventar:").pack(pady=5)
        self.entry_cod = tk.Entry(root)
        self.entry_cod.pack(pady=5)

        tk.Button(root, text="Împrumută Echipament", bg="lightblue", command=self.apasa_imprumut).pack(pady=10)
        self.incarca_date()

    def incarca_date(self):
        self.lista_echipamente.delete(0, tk.END)
        for e in self.lab._Laborator__echipamente:
            text_afisat = f"{e.nume} | Cod: {e.get_cod_inventar()} | Stare: {e.stare}"
            self.lista_echipamente.insert(tk.END, text_afisat)

    def apasa_imprumut(self):
        cod_introdus = self.entry_cod.get()
        utilizator_curent = Student(nume="Utilizator PC", email="user@upt.ro", grupa="2.1")
        rezultat = self.lab.imprumuta_echipament(cod_introdus, utilizator_curent)

        if rezultat:
            messagebox.showinfo("Succes", f"Ai împrumutat echipamentul cu codul {cod_introdus}!")
            self.entry_cod.delete(0, tk.END)
            self.incarca_date()
        else:
            messagebox.showwarning("Eroare", "Cod invalid sau echipament indisponibil. Verifică lista!")

if __name__ == "__main__":
    lab = Laborator("Sisteme Electronice")
    lab.adauga_echipament(Echipament(nume="Osciloscop Digital", cod_inventar="OSC-001"))
    lab.adauga_echipament(Echipament(nume="Multimetru Fluke", cod_inventar="MULT-102"))
    lab.adauga_echipament(Echipament(nume="Sursa Tensiune", cod_inventar="SUR-04", stare="Defect"))
    fereastra = tk.Tk()
    app = InterfataLaborator(fereastra, lab)
    fereastra.mainloop()