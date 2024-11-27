class InventarioMagico:
    def __init__(self):
        self.inventario = []

    def adicionar_item(self, item):
        self.inventario.append(item)
        return f"Item '{item}' adicionado com sucesso."

    def remover_item(self, item):
        if item in self.inventario:
            self.inventario.remove(item)
            return f"Item '{item}' removido com sucesso."
        else:
            return f"Erro: Item '{item}' não encontrado no inventário."

    def listar_itens(self):
        if not self.inventario:
            return "Inventário vazio."
        else:
            return "Itens no inventário:\n" + "\n".join(self.inventario)
