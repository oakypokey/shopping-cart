from shopping_cart import find_product

def test_find_product_valid():
    try:
        result = find_product("1")
        assert result.serial == "1" and result.name == "Chocolate Sandwich Cookies"
    except:
        assert False

def test_find_product_invalid():
    try:
        result = find_product("40")
        assert False
    except:
        assert True

