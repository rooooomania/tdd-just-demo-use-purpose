# app.py
from app import app

def test_always_passes():
    # 常に成功するテスト
    assert True
    
def x_test_always_fails():
    # 常に失敗するテスト (無効化されている)
    assert False

def test_hello_world():
    # ルートエンドポイントにGETリクエストを送信してレスポンスをテストする
    with app.test_client() as client:
        response = client.get('/')
        
        # レスポンスデータが'Hello, World!'であることをテストする
        assert response.data == b'Hello, World!'
        
        # レスポンスステータスコードが200であることをテストする
        assert response.status_code == 200

# def test_parrot():
#     # /parrotエンドポイントにGETリクエストを送信してレスポンスをテストする
#     with app.test_client() as client:
#         say_text = "Hello, Parrot!"
#         response = client.get('/parrot', query_string={'say': say_text})
        
#         # レスポンスステータスコードが200であることをテストする
#         assert response.status_code == 200
        
#         # レスポンスデータがクエリパラメータの内容と一致することをテストする
#         assert response.data.decode('utf-8') == say_text