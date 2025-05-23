from flask import Flask, request, Response
import requests
import os

app = Flask(__name__)

@app.route("/")
def proxy():
    target = request.args.get("url")
    if not target or "bybit.com" not in target:
        return Response("Invalid or missing 'url' parameter", status=400)

    try:
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json"
        }
        r = requests.get(target, headers=headers, timeout=10)
        return Response(r.content, status=r.status_code, content_type="application/json")
    except Exception as e:
        return Response(str(e), status=500)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # ⬅️ Render укажет свой порт здесь
    app.run(host="0.0.0.0", port=port)        # ⬅️ Делаем его доступным извне
