import subprocess

backend = './app.py'
frontend = './ui/main.py'


try:
    subprocess.Popen(['python', frontend], shell=True)
except subprocess.CalledProcessError as e:
    print(f'Error running {frontend}: {e}')
else:
    print(f'{frontend} completed succesfuly')

try:
    subprocess.run(['python', backend], check=True)
except subprocess.CalledProcessError as e:
    print(f'Error running {backend}: {e}')
else:
    print(f'{backend} completed succesfuly')
