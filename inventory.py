# inventory.py

class DatabaseError(Exception):
    """データベース操作時のエラー"""
    pass

class ProductNotFoundException(Exception):
    """商品が見つからないエラー"""
    pass

def register_product(db, product_details):
    """商品情報をデータベースに登録する"""
    if not product_details['name'] or product_details['price'] <= 0:
        raise ValueError("Invalid product details")
    product_id = db.insert('products', product_details)
    return product_id

def initialize_inventory(db, product_id, initial_stock):
    """商品の在庫を初期化する"""
    if initial_stock < 0:
        raise ValueError("Initial stock must be non-negative")
    if not db.exists('products', product_id):
        raise ProductNotFoundException("Product not found")
    db.insert('inventory', {'product_id': product_id, 'stock': initial_stock})
    return True

"""
商品情報登録
商品情報を登録し、在庫の初期化を行う関数
"""
def register_product_and_initialize_inventory(db, product_details, initial_stock):
    """商品情報を登録し、在庫を初期化する"""
    try:
        
        product_id = register_product(db, product_details)
        initialize_inventory(db, product_id, initial_stock)
        return product_id
    except:
        # どちらかの処理でエラーが発生した場合はロールバック
        db.rollback()
        raise DatabaseError("Failed to register product and initialize inventory")
    