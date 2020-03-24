from shopping_cart import calculate_total_price

basket = ["1", "5", "7", "3"]

def calculate_total_price_subtotal_test():
    result = calculate_total_price(basket)["subtotal"]
    assert result == 0.00
