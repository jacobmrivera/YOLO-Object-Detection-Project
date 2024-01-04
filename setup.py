import subprocess
import sys
import venv

def create_virtual_environment():
    venv.create('venv', system_site_packages=False, with_pip=True)

def install_dependencies():
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

if __name__ == "__main__":
    create_virtual_environment()
    install_dependencies()