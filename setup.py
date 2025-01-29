import os
import subprocess
import sys

if os.path.exists('requirements.txt'):
    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

script_path = os.path.abspath('service.py')
python_executable = sys.executable
task_name = 'RunPythonServiceAtStartup'
bat_filename = os.path.join(os.environ['APPDATA'],
                            'Microsoft\\Windows\\Start Menu\\Programs\\Startup',
                            f'{task_name}.bat')
with open(bat_filename, 'w') as bat_file:
        bat_file.write(f'@echo off\n"{python_executable}" "{script_path}"\n')

print(f'Windows task created at {bat_filename}')