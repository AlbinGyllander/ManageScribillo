import subprocess
import psutil
import os
os.system('')  # This line enables the ANSI escape codes on Windows.
virtualenv_path = "C:\\Users\\algy.pa\\Documents\\env\\Scripts\\activate"
working_directory = "C:\\Users\\algy.pa\\Documents\\GitHub\\scribilloAPI\\api"
django_command = "python manage.py runserver"

def kill_process_and_window(process_name):
    process_found = False   
    # Try to terminate the process gracefully
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmdline = process.info['cmdline']
            if cmdline and process_name in cmdline:

                # Kill associated command prompt window
                subprocess.run(f'taskkill /F /FI "WindowTitle eq {process_name} - Command Prompt"', shell=True)
                # Terminate the process
                psutil.Process(process.info['pid']).terminate()
                process_found = True
        except Exception as e:
            
            print(f"Error terminating process {process.info['pid']}: {e}")
            process_found = False
    return process_found
check_intention = input("Are you sure you want to restart Django, this may lead to loss of data? (y/n) ")
if check_intention == 'y':
    # Kill the old Django process
    if kill_process_and_window('manage.py'):
        # Start a new Django process
        command = f'start cmd.exe /k "{virtualenv_path} && cd {working_directory} && {django_command}"'
        subprocess.run(command, shell=True)
    else:
        print("No Django processes found.")
    print("\033[92mRestart completed.\033[0m")
else:
    print("Aborting restart...")
    exit()



