from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>My Hobbies</h1>
    <p>my hobby is travelling.listening a music</p>
    <img src="https://picsum.photos/300" alt="Welcome Image">
    '''

if __name__ == "__main__":
    app.run(debug=True)