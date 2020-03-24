from shopping_cart import find_product

def test_find_product_validID():
    try:
        result = find_product("1")
        assert result.serial == "1" and result.name == "Chocolate Sandwich Cookies"
    except:
        assert False

def test_find_product_invalidID():
    try:
        find_product("40")
        assert False
    except:
        assert True

def test_find_product_typeNumber():
    try:
        find_product(1)
        assert False
    except:
        assert True

