class Product:
    def __init__(self, name, price, quantity, discount, shipping):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount = discount
        self.shipping = shipping

    def PrintInfo(self):
        print("Nome: " + self.name + "\nPreço: R$ " + str(self.price))

# Ctrl + K / Ctrl + C = Comment
# Ctrl + K / Ctrl + U = Uncomment
    # def UpdateName

    # def UpdateQuantity(self, newQuantity):

    # def UpdatePrice

    # def UpdateShipping




produtoA = Product("Computador", 999.90, 10, 0.10, 100.00)
produtoA.PrintInfo()