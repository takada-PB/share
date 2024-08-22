from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # ここに外部データベースにログイン情報を送信するコードを追加します。
    # 例: requests.post(external_db_url, json={"username": username, "password": password})

    # ログインが失敗した場合の応答
    return jsonify({"message": "Login failed"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
