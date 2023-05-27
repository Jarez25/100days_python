import subprocess
import getpass
import os


output_file = r'c:\Users\ADMIN\Desktop\100days_python\DIA 23\dump.sql' #ruta para guardar la base

password = getpass.getpass("Enter MySQL password: ") #solicitar la contra ocullta con el getpass


command = [ #respado de la base de datos
    'mysqldump',
    '--user=root',
    f'--defaults-file={os.path.expanduser("~")}/.my.cnf',
    '--databases',
    'world'
]


with open(output_file, 'w') as out:
    subprocess.Popen(command, stdout=out)
