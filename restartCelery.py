import subprocess
import psutil
import os
os.system('')  # This line enables the ANSI escape codes on Windows.
virtualenv_path = "C:\\Users\\algy.pa\\Documents\\env\\Scripts\\activate"
working_directory = "C:\\Users\\algy.pa\\Documents\\GitHub\\scribilloAPI\\api"
celery_command = "celery -A api worker -l info --pool=solo"

def kill_process_and_window(process_name):
    process_found = False
    try:
        # Terminate all processes with the specified image name
        subprocess.run(f'taskkill /F /IM {process_name}', shell=True)

        # Get the list of all command prompts with 'celery' and 'worker' in the title
        cmd = 'wmic process where "name=\'cmd.exe\' and CommandLine like \'%celery%\' and CommandLine like \'%worker%\'" get ProcessId'
        result = subprocess.check_output(cmd, shell=True).decode().split('\n')[1:-1]
        
        # Terminate each identified process
        for pid in result:
            pid = pid.strip()
            if pid and psutil.pid_exists(int(pid)):
                print("Found process with PID: ", pid)
                subprocess.run(f'taskkill /F /PID {pid}', shell=True)
                process_found = True    
        
        return process_found
    except Exception as e:
        print(f"Error: {e}")
        return False


print("\033[94mINFO: Celery is the task queue used to process audio files and transcribe them.\033[0m")
print("\033[91mWARNING: If there are any active Celery processes, they will be terminated.\033[0m")
check_intention = input("Are you sure you want to restart Celery, this may lead to loss of data? (y/n) ")
if check_intention == 'y':
    if kill_process_and_window('celery.exe'):
        command = f'start cmd.exe /k "{virtualenv_path} && cd {working_directory} && {celery_command}"'
        subprocess.run(command, shell=True)
    else:
        print("No Celery processes found.")

    print("\033[92mRestart completed.\033[0m")
else:
    print("Aborting restart...")
    exit()




