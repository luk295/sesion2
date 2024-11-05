# Crear un programa que recoja por parámetro una ruta y una palabra clave y 
# termine con error ( sys.exit(n) ) en caso de que un archivo o más en el
# directorio contenga esa palabra clave
#
# Tip 1: Comando egrep de linux, método walk de la librería os, etc.
# Tip 2: Códigos de salida con error para github
# https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions


import sys
import subprocess

def main():
	ruta = sys.argv[1]
	contenido = sys.argv[2]
	result = subprocess.run(['egrep', '-R', contenido, ruta], capture_output=True, text=True)
	print(result)
	if (result.returncode == 0):
		sys.exit(1)
if _name_ == "_main_":
	if len(sys.argv) != 3:
		print("Uso: python secret_finder_2.py <ruta> <contenido>")
		sys.exit(1)
	main()
