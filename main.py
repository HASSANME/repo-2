import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Python Flask World V1.0 from CI/CD pipeline'

if __name__ == '__main__':
    # Use the PORT environment variable provided by App Engine, default to 8080 for local testing
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
