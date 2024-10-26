from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/start-vm')
def start_vm():
    try:
        # Run the VBoxManage command to start the virtual machine
        result = subprocess.run(["VBoxManage", "startvm", "your-vm-name", "--type", "headless"], check=True, capture_output=True)
        return "Virtual machine started successfully!"
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
