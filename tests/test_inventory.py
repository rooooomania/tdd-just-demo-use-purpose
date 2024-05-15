# test_inventory.py

import pytest
from inventory import register_product, initialize_inventory, ProductNotFoundException, register_product_and_initialize_inventory, DatabaseError

"""
register_product 関数のテスト
"""
def test_register_product(mocker):
    db = mocker.MagicMock()
    db.insert.return_value = 1  # 商品IDとして1を返す
    product_details = {'name': 'テスト商品', 'price': 1000}
    
    # register_product関数が正しく商品を登録し、商品IDを返すことをテストする
    assert register_product(db, product_details) == 1
    db.insert.assert_called_once_with('products', product_details)

def test_register_product_with_invalid_details(mocker):
    db = mocker.MagicMock()
    product_details = {'name': '', 'price': -100}
    
    # 無効な商品詳細を渡した場合、register_product関数がValueErrorを投げることをテストする
    with pytest.raises(ValueError):
        register_product(db, product_details)

"""
initialize_inventory 関数のテスト
"""
def test_initialize_inventory(mocker):
    db = mocker.MagicMock()
    db.exists.return_value = True
    
    # initialize_inventory関数が正しく在庫を初期化し、Trueを返すことをテストする
    assert initialize_inventory(db, 1, 100) is True
    db.insert.assert_called_once_with('inventory', {'product_id': 1, 'stock': 100})

def test_initialize_inventory_with_nonexistent_product(mocker):
    db = mocker.MagicMock()
    db.exists.return_value = False
    
    # 存在しない商品IDを渡した場合、initialize_inventory関数がProductNotFoundExceptionを投げることをテストする
    with pytest.raises(ProductNotFoundException):
        initialize_inventory(db, 9999, 100)

def test_initialize_inventory_with_negative_stock(mocker):
    db = mocker.MagicMock()
    
    # 負の在庫数を渡した場合、initialize_inventory関数がValueErrorを投げることをテストする
    with pytest.raises(ValueError):
        initialize_inventory(db, 1, -10)

"""
register_product_and_initialize_inventory 関数のテスト
"""
def test_register_product_and_initialize_inventory(mocker):
    db = mocker.MagicMock()
    db.insert.return_value = 1  # register_productが成功した場合
    db.exists.return_value = True  # initialize_inventoryが成功した場合
    product_details = {'name': 'テスト商品', 'price': 1000}
    
    # register_product_and_initialize_inventory関数が正しく商品を登録し、在庫を初期化することをテストする
    assert register_product_and_initialize_inventory(db, product_details, 100) == 1
    db.insert.assert_any_call('products', product_details)
    db.insert.assert_any_call('inventory', {'product_id': 1, 'stock': 100})

def test_register_product_with_error(mocker):
    db = mocker.MagicMock()
    db.insert.return_value = 1  # register_productが成功した場合
    db.exists.return_value = False  # initialize_inventoryが失敗した場合
    product_details = {'name': 'テスト商品', 'price': 1000}
    
    # 商品登録が成功し在庫初期化が失敗した場合、ロールバックが行われ、DatabaseErrorが投げられることをテストする
    with pytest.raises(DatabaseError):
        register_product_and_initialize_inventory(db, product_details, 100)
    db.rollback.assert_called_once()

def test_initialize_inventory_with_error(mocker):
    db = mocker.MagicMock()
    db.insert.side_effect = [1, DatabaseError]  # initialize_inventoryが失敗した場合
    db.exists.return_value = True  # register_productが成功した場合
    product_details = {'name': 'テスト商品', 'price': 1000}
    
    # 商品登録が成功し在庫初期化が失敗した場合、ロールバックが行われ、DatabaseErrorが投げられることをテストする
    with pytest.raises(DatabaseError):
        register_product_and_initialize_inventory(db, product_details, 100)
    db.rollback.assert_called_once()
