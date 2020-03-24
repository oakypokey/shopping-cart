from shopping_cart import calculate_total_price

basket1 = ["1", "5", "7", "3"]

def test_calculate_total_price_basket1_subtotal():
    result = calculate_total_price(basket1)["subtotal"]
    assert result == 17.48

def test_calculate_total_price_basket1_tax():
    result = calculate_total_price(basket1)["tax"]
    assert result == 1.5294999999999999

def test_calculate_total_price_basket1_total():
    result = calculate_total_price(basket1)["total"]
    assert result == 19.009500000000003

basket2 = ["5", "10", "3", "3"]

def test_calculate_total_price_basket2_subtotal():
    result = calculate_total_price(basket2)["subtotal"]
    assert result == 15.96

def test_calculate_total_price_basket2_tax():
    result = calculate_total_price(basket2)["tax"]
    assert result == 1.3965

def test_calculate_total_price_basket2_total():
    result = calculate_total_price(basket2)["total"]
    assert result == 17.3565