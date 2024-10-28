from flask import Flask, render_template
from analytics import get_active_users

app = Flask(__name__)

@app.route('/')
def home():
    active_users = get_active_users()
    return render_template('index.html', active_users=active_users)

if __name__ == '__main__':
    app.run(debug=True)
