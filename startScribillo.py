import subprocess

# Replace with the absolute path to your virtual environment's activate script
virtualenv_path = "C:\\Users\\algy.pa\\Documents\\env\\Scripts\\activate"

# Replace with the absolute path to your project's directory
working_directory = "C:\\Users\\algy.pa\\Documents\\GitHub"

# Replace with the actual commands to run your services
django_command = "python manage.py runserver"
svelte_command = "npm run dev"
celery_command = "celery -A api worker -l info --pool=solo"

commands = [
    f'start cmd.exe /k "{virtualenv_path} && cd {working_directory}/scribilloAPI/api && {django_command}"',
    f'start cmd.exe /k "{virtualenv_path} && cd {working_directory}/FlowbiteSvelte/Scribillo && {svelte_command}"',
    f'start cmd.exe /k "{virtualenv_path} && cd {working_directory}/scribilloAPI/api && {celery_command}"',
]

for command in commands:
    subprocess.Popen(command, shell=True)

input("Press Enter to exit...")
