import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from inventario import InventarioMagico

class InventarioGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(" ")
        self.root.geometry("1075x614")

        self.background_image = ImageTk.PhotoImage(Image.open("assets/background.png"))
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.inventario = InventarioMagico()

        self.title_frame = tk.Frame(root, bg="#2b2b2b", highlightbackground="#388E3C", highlightthickness=3)
        self.title_frame.place(relx=0.5, y=30, anchor="center", width=500, height=50)

        self.label_title_shadow = tk.Label(
            self.title_frame,
            text="Inventário Mágico 🪄",
            font=("Helvetica", 24, "bold"),
            fg="#1A1A1A",
            bg="#2b2b2b",
        )
        self.label_title_shadow.place(relx=0.505, rely=0.505, anchor="center")

        self.label_title = tk.Label(
            self.title_frame,
            text="Inventário Mágico 🪄",
            font=("Helvetica", 24, "bold"),
            fg="#FFD700",
            bg="#2b2b2b",
        )
        self.label_title.place(relx=0.5, rely=0.5, anchor="center")

        self.output_frame = tk.Frame(root, bg="#2b2b2b", highlightthickness=2, highlightbackground="#388E3C")
        self.output_frame.place_forget()

        self.text_scrollbar = tk.Scrollbar(self.output_frame, orient="vertical")

        self.text_output = tk.Text(
            self.output_frame,
            font=("Courier", 14),
            width=50,
            height=5,
            state="disabled",
            bg="#2b2b2b",
            fg="#FFD700",
            insertbackground="#FFD700",
            highlightthickness=0,
            yscrollcommand=self.text_scrollbar.set,
        )
        self.text_output.pack(side="left", fill="both", expand=True)

        self.close_output_button = tk.Button(
            self.output_frame,
            text="✖",
            font=("Helvetica", 12, "bold"),
            bg="#1B5E20", fg="#FFD700",
            bd=0, highlightthickness=0,
            command=self.fechar_saida
        )

        self.entry_item = tk.Entry(
            root,
            font=("Helvetica", 14),
            width=40,
            bg="#2b2b2b",
            fg="#FFD700",
            insertbackground="#FFD700",
            highlightthickness=2,
            highlightbackground="#388E3C",
            highlightcolor="#66BB6A",
        )
        self.entry_item.place(relx=0.5, rely=0.8, anchor="center")

        self.icon_add = ImageTk.PhotoImage(Image.open("assets/add.png").resize((50, 50)))
        self.icon_remove = ImageTk.PhotoImage(Image.open("assets/remove.png").resize((50, 50)))
        self.icon_list = ImageTk.PhotoImage(Image.open("assets/list.png").resize((50, 50)))
        self.icon_exit = ImageTk.PhotoImage(Image.open("assets/exit.png").resize((50, 50)))

        self.button_add = self.create_hover_button(root, self.icon_add, "Adicionar item", self.adicionar_item, 0.35)
        self.button_remove = self.create_hover_button(root, self.icon_remove, "Excluir item", self.remover_item, 0.45)
        self.button_list = self.create_hover_button(root, self.icon_list, "Listar itens", self.listar_itens, 0.55)
        self.button_exit = self.create_hover_button(root, self.icon_exit, "Sair", self.sair, 0.65)

    def create_hover_button(self, root, icon, tooltip_text, command, relx_position):
        button = tk.Button(
            root, image=icon, command=command,
            bg="#0D3A16", activebackground="#1B5E20", bd=0, relief="flat", highlightthickness=0
        )
        button.place(relx=relx_position, rely=0.9, anchor="center")

        tooltip = tk.Label(
            root, text=tooltip_text, font=("Helvetica", 10, "italic"),
            bg="#2b2b2b", fg="#FFD700", relief="solid", borderwidth=1, padx=5, pady=2
        )
        tooltip.place_forget()

        def on_enter(e):
            button.config(bg="#1B5E20", relief="raised")
            tooltip.place(relx=relx_position, rely=0.85, anchor="center")

        def on_leave(e):
            button.config(bg="#0D3A16", relief="flat")
            tooltip.place_forget()

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

        return button

    def exibir_saida(self, texto, delay=None):
        self.output_frame.place(relx=0.5, rely=0.6, anchor="center")
        self.text_output.configure(state="normal")
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, texto)
        self.text_output.configure(state="disabled")
        if int(self.text_output.index('end-1c').split('.')[0]) > 10:
            self.text_scrollbar.pack(side="right", fill="y")
        else:
            self.text_scrollbar.pack_forget()
        if delay is None:
            self.close_output_button.place(relx=1.0, rely=0.0, anchor="ne", x=-5, y=5)
        else:
            self.close_output_button.place_forget()
            self.output_frame.after(delay, self.fechar_saida)

    def fechar_saida(self):
        self.output_frame.place_forget()

    def adicionar_item(self):
        item = self.entry_item.get().strip()
        if item:
            mensagem = self.inventario.adicionar_item(item)
            self.exibir_saida(mensagem, delay=2000)
            self.entry_item.delete(0, tk.END)
        else:
            self.exibir_saida("Digite um nome para o item.", delay=1500)

    def remover_item(self):
        item = self.entry_item.get().strip()
        if item:
            mensagem = self.inventario.remover_item(item)
            self.exibir_saida(mensagem, delay=2000)
            self.entry_item.delete(0, tk.END)
        else:
            self.exibir_saida("Digite o nome do item para remover.", delay=1500)

    def listar_itens(self):
        itens = self.inventario.listar_itens()
        self.exibir_saida(itens)

    def sair(self):
        self.root.destroy()

    def mostrar_mensagem(self, mensagem):
        messagebox.showinfo("Inventário Mágico", mensagem)


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    app = InventarioGUI(root)
    root.mainloop()
