import tkinter as tk
from tkinter import messagebox
from proiect import Student, Echipament, Laborator


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