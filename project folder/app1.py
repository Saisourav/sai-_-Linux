from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form['user_input']
    # Do whatever processing you want with user_input
    # For example, you can print it or use it in any other way
    print(f"User input: {user_input}")
    return 'Input received successfully!'

if __name__ == '__main__':
    app.run()
