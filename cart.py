echo "class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append({'item': item, 'price': price})
        print(f'Добавлено в корзину: {item} за {price} руб.')

    def show_cart(self):
        if not self.items:
            print('Корзина пуста')
        else:
            print('Товары в корзине:')
            for item in self.items:
                print(f'- {item['item']}: {item['price']} руб.')

# Пример использования
if __name__ == '__main__':
    cart = ShoppingCart()
    cart.add_item('Ноутбук', 50000)
    cart.add_item('Мышь', 1500)
    cart.show_cart()" > cart.py
