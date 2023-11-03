import os
import subprocess
import sys

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing: {command}")
        print(f"Output: {result.stdout}")
        print(f"Error message: {result.stderr}")
        return None
    return result.stdout
def clone_repo(path):
    print(f"Cloning GitHub repository form {path}...", flush=True)
    result = run_command(f"git clone {path}")
    if result is not None:
        print("Successfully cloned the repository.", flush=True)
    else:
        print("Failed to clone the repository.", flush=True)


# Check if Python 3.11 is already installed
def find_python_in_path():
    for path_dir in os.environ["PATH"].split(os.pathsep):
        potential_python = os.path.join(path_dir, "python.exe")
        if os.path.exists(potential_python):
            version = run_command(f'"{potential_python}" --version')
            if "Python 3.11" in version:
                return True
    return False


if find_python_in_path():
    print("Python 3.11 is already installed.",flush=True)
else:
    print("Python 3.11 is not installed. Proceeding with installation.",flush=True)
    
    # Define the desired Python version and installer details
    PYTHON_VERSION = "3.11.4"
    installer_url = f"https://www.python.org/ftp/python/{PYTHON_VERSION}/python-{PYTHON_VERSION}-amd64.exe"
    installer_name = f"python-{PYTHON_VERSION}-amd64.exe"
    
    # Download the Python installer
    download_command = f'powershell -Command "Invoke-WebRequest -Uri {installer_url} -OutFile .\\{installer_name}"'
    run_command(download_command)
    
    # Install Python
    run_command(f"{installer_name} /quiet InstallAllUsers=1 PrependPath=1")



# Define the Python version, installation path, and your GitHub repo URL
PYTHON_INSTALL_PATH = r"C:\Users\albin\AppData\Local\Programs\Python\Python311"
PYTHON_EXECUTABLE_PATH = os.path.join(PYTHON_INSTALL_PATH, "python.exe")

GITHUB_BACKEND_REPO_URL = "git@github.com:AlbinGyllander/scribilloAPI.git"
GITHUB_FRONTEND_REPO_URL = "git@github.com:AlbinGyllander/FlowbiteSvelte.git"

# # Path to the virtual environment directory
VENV_PATH = "scribilloENV"

VENV_PYTHON = os.path.join(VENV_PATH, "Scripts", "python.exe")

 # Check if the virtual environment already exists
if os.path.exists(VENV_PATH):
    print(f"Virtual environment at {VENV_PATH} already exists.",flush=True)
else:
    # Create the virtual environment
    run_command(f'"{PYTHON_EXECUTABLE_PATH}" -m venv "{VENV_PATH}"')

# Install requirements one-by-one for feedback
print("Installing requirements...",flush=True)
print("Python exe:")
print(PYTHON_EXECUTABLE_PATH)
total_packages = 0
successful_installs = 0
failed_installs = 0

with open("requirements.txt", "r") as req_file:
    for line in req_file:
        package = line.strip()
        if package and not package.startswith("#"):  # Ensure it's not an empty line or a comment
            total_packages += 1
            print(f"Installing {package}...", flush=True)
            result = run_command(f'"{VENV_PYTHON}" -m pip install "{package}"')
            if result is not None:
                print(f"Finished installing {package}.", flush=True)
                successful_installs += 1
            else:
                print(f"Failed to install {package}.", flush=True)
                failed_installs += 1

print(f"\nFinished installing {total_packages} packages. {successful_installs} successful, {failed_installs} failed.", flush=True)



# Clone the GitHub repository
clone_repo(GITHUB_BACKEND_REPO_URL)
clone_repo(GITHUB_FRONTEND_REPO_URL)
print("Downloading RabbitMQ",flush=True)
run_command("choco install rabbitmq")

print("Installing FFMPEG",flush=True)
run_command("choco install ffmpeg")






