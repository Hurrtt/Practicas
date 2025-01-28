# Practicas
¡Perfecto! Aquí tienes un ejercicio pensado para que trabajen en equipo y practiquen Python, bases de datos y GitHub:

Ejercicio: Sistema de Gestión de Tareas

Descripción:

Crear un programa en Python que gestione tareas usando una base de datos MySQL. El programa debe permitir:
	1.	Agregar tareas con un título, una descripción, una fecha límite y un estado (pendiente/completada).
	2.	Listar tareas mostrando su información.
	3.	Marcar tareas como completadas.
	4.	Eliminar tareas.

Requisitos técnicos:
	•	Usar Python para la lógica del programa.
	•	Conectar el programa a una base de datos MySQL.
	•	Crear un repositorio en GitHub para colaborar.

Distribución de roles:
	1.	Persona 1: Diseño de la base de datos.
	•	Crear la tabla tareas en MySQL con las siguientes columnas:
	•	id (entero, clave primaria, autoincremental).
	•	titulo (texto).
	•	descripcion (texto).
	•	fecha_limite (fecha).
	•	estado (texto, valores posibles: “pendiente” o “completada”).
	•	Documentar cómo crear la base de datos y la tabla para que los demás puedan configurarla.
	2.	Persona 2: Funciones CRUD en Python.
	•	Escribir las funciones para interactuar con la base de datos:
	•	agregar_tarea().
	•	listar_tareas().
	•	marcar_completada(id_tarea).
	•	eliminar_tarea(id_tarea).
	3.	Persona 3: Interfaz de usuario en consola.
	•	Crear un menú en consola que permita al usuario:
	1.	Agregar una nueva tarea.
	2.	Ver todas las tareas.
	3.	Marcar una tarea como completada.
	4.	Eliminar una tarea.
	•	Integrar las funciones de Persona 2.
	4.	Persona 4: Gestión del proyecto en GitHub.
	•	Crear el repositorio en GitHub.
	•	Dividir las tareas entre los integrantes.
	•	Revisar y fusionar los cambios.
	•	Escribir un archivo README.md con las instrucciones para usar el programa.

Tareas adicionales:
	•	Colaboración:
	•	Cada persona debe subir su trabajo a una rama en GitHub.
	•	Realizar revisiones de código (pull requests).
	•	Pruebas:
	•	Probar el programa en equipo y corregir errores.
	•	Extras (opcional):
	•	Agregar validaciones (ejemplo: que no se agreguen tareas sin título).
	•	Usar datetime en Python para verificar fechas.

¿Quieren que les detalle alguna parte o les ayudo con el diseño de la base de datos o el código inicial? 🚀
