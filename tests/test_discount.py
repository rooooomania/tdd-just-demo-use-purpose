from discount import calculate_discounted_price
import pytest

def test_calculate_discounted_price():
    # 正常な割引計算
    assert calculate_discounted_price(1000, 20) == 800
    assert calculate_discounted_price(2000, 50) == 1000
    assert calculate_discounted_price(500, 10) == 450

def test_calculate_discounted_price_with_no_discount():
    # 割引率が0%の場合
    assert calculate_discounted_price(1000, 0) == 1000

def test_calculate_discounted_price_with_full_discount():
    # 割引率が100%の場合
    assert calculate_discounted_price(1000, 100) == 0

def test_calculate_discounted_price_with_invalid_discount():
    # 不正な割引率でエラーをテスト
    with pytest.raises(ValueError):
        calculate_discounted_price(1000, -1)
    with pytest.raises(ValueError):
        calculate_discounted_price(1000, 101)

def test_calculate_discounted_price_with_invalid_price():
    # 不正な価格でエラーをテスト
    with pytest.raises(ValueError):
        calculate_discounted_price(-1, 10)
    with pytest.raises(ValueError):
        calculate_discounted_price(1000, -10)
            