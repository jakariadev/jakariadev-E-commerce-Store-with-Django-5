from decimal import Decimal
from store.models import Product


class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("session_key")

        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        self.cart = cart

    def add(self, product, product_qty):
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_qty

        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': product_qty}

        self.session.modified = True

    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())

    def __iter__(self):
        all_product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=all_product_ids)
        import copy
        cart = copy.deepcopy(self.cart)

        # cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

            print("_____: ", cart)

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total'] = item['price'] * item['qty']
            print(item)
            yield item

    def get_total(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())

    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

    def update(self, product_id, qty):
        product_id = str(product_id)
        product_quantity = int(qty)

        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_quantity
            print("The values are updated . . . . . . . . . . .: ", product_id)
            print("The values are updated . . . . . . . . . . . Qty: ", product_quantity)

        # else:
        #     self.cart[product_id] = {'price': str(product.price), 'qty': product_quantity}

        self.session.modified = True
