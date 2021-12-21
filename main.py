import requests


# Recordar, pagina: http://127.0.0.1:8880/form o http://localhost:8880/form

mensaje = {  }

''' Podemos saber que las claves son "name", "email" y "message"
por el codigo HTML de la pagina como vimos anteriormente:

No encontre el archivo que decia el enunciado en el Alumni
"webformlab.py", por lo que lo hago con el archivo visto
"webform.py" y reemplazo lo de enviar una inscripcion por enviar
un mensaje. '''

mensaje['name'] = input("Nombre: ")
mensaje['email'] = input("Email: ")
mensaje['message'] = input("Mensaje: ")

respuesta = requests.post("http://127.0.0.1:8880/form",
	data = mensaje
)

contenido_respuesta = respuesta.content.decode("utf-8")

print(respuesta.status_code) # Imprime 200.

if "Mensaje enviado correctamente" in contenido_respuesta:
	print("¡Alumno inscripto correctamente!\n")
else:
	print("Debes ingresar todos los campos.")

input("Ingrese lo que sea para salir: ")