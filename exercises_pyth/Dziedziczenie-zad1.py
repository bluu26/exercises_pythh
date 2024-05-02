class Cart:
    def __init__(self):
        self.products = []

    def add(self, price, name):
        self.products.append([price, name])

    def summary(self, ):
        return self.products


class Discount20PercentCart(Cart):
    def summary(self):
        discounted_products = []
        for price, name in self.products:
            discounted_price = price * 0.8  # 20% discount
            discounted_products.append((discounted_price, name))
            # for product in self.products:
            # nowa_cena = product[0] * 0.8
            # discount_products.append(nowa_cena, product[1]))
        return discounted_products


# class Above3ProductsCheapestFreeCart(Cart):
#     def summary(self):
#         if len(self.products) < 3:
#             # cheapest_index = min(range(len(self.products)), key=lambda i: self.products[i][0])
#             # # Zmień cenę najtańszego produktu na zero
#             # self.products[cheapest_index][0] = 0
#             return self.products
#         else:
#             sorted_list = sorted(self.products)
#             sorted_list[0] = (0, sorted_list[0][1])
#             return sorted_list

class Above3ProductsCheapestFreeCart(Cart):
    def summary(self):
        if len(self.products) < 3:
            return self.products
        else:
            index_low = 0
            index = 0
            for item in self.products[1:]:
                if self.products[index_low][0] > item[0]:
                    index_low = index
                index += 1
                self.products[index_low] = (0, self.products[index_low][1])
                return self.products



cart1 = Cart()
cart1.add(100, 'Mleko')
cart1.add(10, 'Kisiel')
cart1.add(20, 'Klej')
cart1.add(201, 'drzewo')
print("Cart summary:")
print(cart1.summary())
print("--------------------------------------")
cart2 = Discount20PercentCart()
cart2.add(100, 'Mleko')
cart2.add(10, 'Kisiel')
cart2.add(20, 'Klej')
cart2.add(201, 'drzewo')
print("Cart summary:")
print(cart2.summary())
print("--------------------------------------")
cart2 = Discount20PercentCart()
cart2.add(100, 'Mleko')
cart2.add(10, 'Kisiel')
cart2.add(20, 'Klej')
cart2.add(201, 'drzewo')
print("Cart summary:")
print(cart2.summary())
