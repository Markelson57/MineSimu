import subprocess

def simular_mineria():
    # Ejecutar el comando para iniciar la simulación de minería
    comando = "python3 Mine.py"  # Reemplaza "tu_archivo_de_simulacion.py" por el nombre de tu archivo de simulación
    proceso = subprocess.Popen(comando, shell=True)
    proceso.communicate()  # Esperar a que el proceso finalice

# Llamar a la función para simular la minería
simular_mineria()
