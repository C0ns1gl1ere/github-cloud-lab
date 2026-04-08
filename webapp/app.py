from flask import Flask
import os, redis
app = Flask(__name__)
cache = redis.Redis(host=os.environ.get("REDIS_HOST", "redis"), port=6379)
@app.route("/")
def index():
    try:
        visits = cache.incr("visits")
    except:
        visits = "unavailable"
    return f"<h1>Docker працює!</h1><p>Кількість відвідувань: <strong>{visits}</strong></p>"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
