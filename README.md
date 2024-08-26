# PROYECTO INTEGRADOR

## Datos del estudiante

- **Nombre:** Anggie Annabell Alava Espinales
- **Materia:** Logica de Programación
- **Carrera:** Ingeniería en Software
- **Nombre del proyecto:** Generador de Contraseñas
- **Pofesora:** Ing. Monica Salazar
- **Semestre:** 1
- **Email de contacto:** analavaes@uide.edu.ec

## Descripción del proyecto

Este es un generador de contraseñas que utiliza el módulo `uuid` y `base64` de Python para crear contraseñas aleatorias y seguras de una longitud especificada. El propósito de esta aplicación es proporcionar una manera fácil y segura de generar contraseñas que cumplan con los estándares de seguridad modernos.

## Requisitos

Para ejecutar este generador de contraseñas, asegúrate de tener Python instalado en tu sistema. Este código es compatible con Python 3.x.

## Instalación

No es necesario instalar ninguna biblioteca adicional, sin embargo si deseas probar el test que evalua el codigo necesitas instalar `pytest`

Corre el siguiente comando en tu terminal:
`pipenv install pytest`

## Uso

El generador de contraseñas está implementado en el siguiente código:

```python
import uuid
import base64

def generate_password(length: int = 16) -> str:
    return base64.b64encode(uuid.uuid4().bytes).decode()[0:length]

print(generate_password())

```

### Puedes viasualizar el diagrama de flujo que describe el proceso del proyecto con esta imagen adjunta:

<img src="https://github.com/user-attachments/assets/bf3feb7b-0665-47fe-9a04-de70ce2a28e9" alt="diagramafinal" width="300" height="500"/>

#### O puedes ingresar al index.html adjunto aqui en el proyecto, y correr el diagrama de forma local en el navegador.

## Correr los test

`pytest -s test.py`

### [VIdeo Tutorial]([https://www.linkedin.com/in/anggiealava/](https://drive.google.com/file/d/1Md6aKCUxfR0DCQCD3m38YQZlRDaeoWzp/view?usp=drive_link))

### [Diapositivas]([https://www.linkedin.com/in/anggiealava/](https://drive.google.com/file/d/16p_9qtJLFf7B0jzK8vzMJu2SED9ZCBdn/view?usp=sharing))
