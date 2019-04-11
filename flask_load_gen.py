from flask import Flask
import subprocess
load_shell_cmd="dd if=/dev/urandom bs=100M count=1 | bzip2 -9 >> /dev/null &"
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return("<h1>Hello!</h1>  Visit /load to generate load")

@app.route('/load', methods=['GET', 'POST'])
def gen_load():

    load_job = subprocess.check_output(['bash','-c', load_shell_cmd])
    return("\nok! Process Started!\n")

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)



