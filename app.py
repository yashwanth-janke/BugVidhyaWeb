from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/editor')
def editor():
    return render_template('Editor/editor.html')

@app.route('/python')
def python():
    return render_template('Python/python.html')

@app.route('/java')
def java():
    return render_template('Java/java.html')

# -------------------------------
@app.route('/python/while')
def variable():
    return render_template('Python/while.html')

@app.route('/python/datatype')
def dtype():
    return render_template('Python/dtype.html')

@app.route('/python/operator')
def op():
    return render_template('Python/op.html')

@app.route('/python/list')
def list():
    return render_template('Python/list.html')

@app.route('/python/tuple')
def tuple():
    return render_template('Python/tuple.html')

@app.route('/python/set')
def set():
    return render_template('Python/set.html')

@app.route('/python/dict')
def dict():
    return render_template('Python/dict.html')

@app.route('/python/conditional')
def conditional():
    return render_template('Python/if.html')

# -------------------------------

@app.route('/java/variables')
def variablej():
    return render_template('Java/variables.html')

@app.route('/java/overloading')
def overloading():
    return render_template('Java/overloading.html')

@app.route('/java/classes')
def classes():
    return render_template('Java/class.html')



@app.route('/java/constructor')
def constructor():
    return render_template('Java/constructor.html')



@app.route('/java/inheritence')
def inheritence():
    return render_template('Java/inheritence.html')



@app.route('/java/polymorphism')
def polymorphism():
    return render_template('Java/polymorphism.html')



@app.route('/java/abstraction')
def abstraction():
    return render_template('Java/abstraction.html')



@app.route('/java/methods')
def methods():
    return render_template('Java/methods.html')



@app.route('/run_code', methods=['POST'])
def run_code():
    if request.method == 'POST':
        data = request.json
        python_code = data['code']

        # Run Python code using subprocess
        result = subprocess.run(['python', '-c', python_code], capture_output=True, text=True)
        output = result.stdout

        return jsonify({'output': output})


if __name__ == '__main__':
    app.run(debug=True)

