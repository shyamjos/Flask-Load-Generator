from flask import Flask
import subprocess
load_shell_cmd="dd if=/dev/urandom bs=100M count=1 | bzip2 -9 >> /dev/null &"
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return("<h1>Hello!</h1>  Visit /load to generate load")

@app.route('/load', methods=['GET', 'POST'])
def gen_load():
    get_hostname = subprocess.check_output(['bash','-c', 'echo "Hostname:" ;hostname; echo " </br> System Load:"; uptime | cut -d ":" -f 5'])
    load_job = subprocess.check_output(['bash','-c', load_shell_cmd])
    response_msg="\nok! Process Started!\n </br>" + str(get_hostname, 'utf-8')
    return (response_msg)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)



