# test_inventory.py

import pytest
from inventory import register_product, initialize_inventory, ProductNotFoundException, register_product_and_initialize_inventory, DatabaseError

def test_register_product(mocker):
    db = mocker.MagicMock()
    db.insert.return_value = 1  # 商品IDとして1を返す
    product_details = {'name': 'テスト商品', 'price': 1000}
    assert register_product(db, product_details) == 1
    db.insert.assert_called_once_with('products', product_details)

def test_register_product_with_invalid_details(mocker):
    db = mocker.MagicMock()
    product_details = {'name': '', 'price': -100}
    with pytest.raises(ValueError):
        register_product(db, product_details)

def test_initialize_inventory(mocker):
    db = mocker.MagicMock()
    db.exists.return_value = True
    assert initialize_inventory(db, 1, 100) is True
    db.insert.assert_called_once_with('inventory', {'product_id': 1, 'stock': 100})

def test_initialize_inventory_with_nonexistent_product(mocker):
    db = mocker.MagicMock()
    db.exists.return_value = False
    with pytest.raises(ProductNotFoundException):
        initialize_inventory(db, 9999, 100)

def test_initialize_inventory_with_negative_stock(mocker):
    db = mocker.MagicMock()
    with pytest.raises(ValueError):
        initialize_inventory(db, 1, -10)
        
def test_register_product_and_initialize_inventory(mocker):
    db = mocker.MagicMock()
    db.insert.return_value = 1  # register_productが成功した場合
    db.exists.return_value = True  # initialize_inventoryが成功した場合
    product_details = {'name': 'テスト商品', 'price': 1000}
    assert register_product_and_initialize_inventory(db, product_details, 100) == 1
    db.insert.assert_any_call('products', product_details)
    db.insert.assert_any_call('inventory', {'product_id': 1, 'stock': 100})
    
# どちらかの処理でエラーが発生した場合、ロールバックしてエラーを投げる
def test_register_product_with_error(mocker):
    db = mocker.MagicMock()
    db.insert.return_value = 1  # register_productが成功した場合
    db.exists.return_value = False  # initialize_inventoryが失敗した場合
    product_details = {'name': 'テスト商品', 'price': 1000}
    with pytest.raises(DatabaseError):
        register_product_and_initialize_inventory(db, product_details, 100)
    db.rollback.assert_called_once()

    
def test_initialize_inventory_with_error(mocker):
    db = mocker.MagicMock()
    db.insert.side_effect = [1, DatabaseError]  # initialize_inventoryが失敗した場合
    db.exists.return_value = True  # register_productが成功した場合
    product_details = {'name': 'テスト商品', 'price': 1000}
    
    with pytest.raises(DatabaseError):
        register_product_and_initialize_inventory(db, product_details, 100)
    db.rollback.assert_called_once()

