from discount import calculate_discounted_price
import pytest

def test_calculate_discounted_price():
    # 正常な割引計算
    # 商品価格が1000円で割引率が20%の場合、割引後の価格が800円であることをテストする
    assert calculate_discounted_price(1000, 20) == 800
    # 商品価格が2000円で割引率が50%の場合、割引後の価格が1000円であることをテストする
    assert calculate_discounted_price(2000, 50) == 1000
    # 商品価格が500円で割引率が10%の場合、割引後の価格が450円であることをテストする
    assert calculate_discounted_price(500, 10) == 450

def test_calculate_discounted_price_with_no_discount():
    # 割引率が0%の場合
    # 商品価格が1000円で割引率が0%の場合、割引後の価格が1000円であることをテストする
    assert calculate_discounted_price(1000, 0) == 1000

def test_calculate_discounted_price_with_full_discount():
    # 割引率が100%の場合
    # 商品価格が1000円で割引率が100%の場合、割引後の価格が0円であることをテストする
    assert calculate_discounted_price(1000, 100) == 0

def test_calculate_discounted_price_with_invalid_discount():
    # 不正な割引率でエラーをテスト
    # 割引率が-1%の場合、ValueErrorが発生することをテストする
    with pytest.raises(ValueError):
        calculate_discounted_price(1000, -1)
    # 割引率が101%の場合、ValueErrorが発生することをテストする
    with pytest.raises(ValueError):
        calculate_discounted_price(1000, 101)

def test_calculate_discounted_price_with_invalid_price():
    # 不正な価格でエラーをテスト
    # 商品価格が-1円の場合、ValueErrorが発生することをテストする
    with pytest.raises(ValueError):
        calculate_discounted_price(-1, 10)
    # 割引率が負の値（例: -10%）の場合、ValueErrorが発生することをテストする
    with pytest.raises(ValueError):
        calculate_discounted_price(1000, -10)
