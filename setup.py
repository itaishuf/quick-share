import os
import subprocess
import sys

if os.path.exists('requirements.txt'):
    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

script_path = os.path.abspath('service.pyw')
python_executable = sys.executable.replace('python', 'pythonw')
task_name = 'RunPythonServiceAtStartup'
vbs_filename = os.path.join(os.environ['APPDATA'],
                            'Microsoft\\Windows\\Start Menu\\Programs\\Startup',
                            f'{task_name}.vbs')

with open(vbs_filename, 'w') as vbs_file:
        vbs_file.write(f'CreateObject("Wscript.Shell").Run """{python_executable}"" ""{script_path}""", 0, True')
# with open(bat_filename, 'w') as bat_file:
#         bat_file.write(f'@echo off\n"{python_executable}" "{script_path}"\n')
print(f'Windows task created at {vbs_filename}')
