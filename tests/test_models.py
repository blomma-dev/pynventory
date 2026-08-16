from pynventory.models import Product


# test if product stores values correctly
def test_product_stores_values():
    product = Product(
        "physical",
        "Fruit",
        "Trader Joe",
        "Green Apple",
        0.10,
        0.20,
        24,
        80,
        20,
    )

    assert product.item_type == "physical"
    assert product.category == "Fruit"
    assert product.brand_name == "Trader Joe"
    assert product.product_name == "Green Apple"
    assert product.price_buy == 0.10
    assert product.price_sell == 0.20
    assert product.tax_percentage == 24
    assert product.weight == 80
    assert product.in_stock == 20


# test if product calculates profit correctly
def test_product_calculates_profit():
    product = Product(
        "physical",
        "Fruit",
        "Trader Joe",
        "Green Apple",
        0.10,
        0.20,
        24,
        80,
        20,
    )

    assert product.profit == 0.10


# test if product id is None by default
def test_product_id_is_none_by_default():
    product = Product(
        "physical",
        "Fruit",
        "Trader Joe",
        "Green Apple",
        0.10,
        0.20,
        24,
        80,
        20,
    )

    assert product.id is None


# test if product keeps provided id
def test_product_keeps_provided_id():
    product = Product(
        "physical",
        "Fruit",
        "Trader Joe",
        "Green Apple",
        0.10,
        0.20,
        24,
        80,
        20,
        5
    )

    assert product.id == 5
