class Product:
    def __init__(self, item_type, category, brand_name, product_name, price_buy, price_sell, tax_percentage, id=None):
        self.id = id
        self.item_type = item_type
        self.category = category
        self.brand_name = brand_name
        self.product_name = product_name
        self.price_buy = price_buy
        self.price_sell = price_sell
        self.tax_percentage = tax_percentage
        self.profit = price_sell - price_buy