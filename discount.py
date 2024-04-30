# discount.py
def calculate_discounted_price(original_price, discount_percentage):
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    discount_amount = (original_price * discount_percentage) / 100
    return original_price - discount_amount