import requests


# Recordar, pagina: http://127.0.0.1:8880/form o http://localhost:8880/form

mensaje = {  }

''' Podemos saber que las claves son "name", "email" y "message"
por el codigo HTML de la pagina. '''

print("""Usted enviara un mensaje desde la pagina \"http://localhost:8880/form\".
Recuerde que debera ejecutar el programa \"webform.py\" en simultaneo con este
para poder acceder a la pagina web.\n""")

mensaje['name'] = input("Nombre: ")
mensaje['email'] = input("Email: ")
mensaje['message'] = input("Mensaje: ")

try:
	respuesta = requests.post("http://127.0.0.1:8880/form",
		data = mensaje
	)
except:
	print("\nERROR: Recuerde ejecutar el programa \"webform.py\" de manera simultanea con este mismo programa, ya que la pagina que se utiliza para enviar el mensaje (http://localhost:8880/form) es hosteada con el mismo \"webform.py\".")
	input("\nIngrese lo que sea para salir: ")
	quit()

# print(respuesta.status_code) # 200 right.

contenido_respuesta = respuesta.content.decode("utf-8")

if "Mensaje enviado correctamente" in contenido_respuesta:
	print("\nEl mensaje ha sido enviado correctamente.\n")
else:
	print("\nERROR: Debes ingresar todos los campos para poder enviar el mensaje.")

input("\nIngrese lo que sea para salir: ")
