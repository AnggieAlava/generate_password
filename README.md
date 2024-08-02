# Generador Seguro de Contraseñas

## Descripción

Este es un generador seguro de contraseñas que utiliza el módulo `uuid` y `base64` de Python para crear contraseñas aleatorias y seguras de una longitud especificada. El propósito de esta aplicación es proporcionar una manera fácil y segura de generar contraseñas que cumplan con los estándares de seguridad modernos.

## Requisitos

Para ejecutar este generador de contraseñas, asegúrate de tener Python instalado en tu sistema. Este código es compatible con Python 3.x.

## Instalación

No es necesario instalar ninguna biblioteca adicional, ya que el código utiliza módulos estándar de Python.

## Uso

El generador de contraseñas está implementado en el siguiente código:

```python
import uuid
import base64

def generate_password(length: int = 16) -> str:
    return base64.b64encode(uuid.uuid4().bytes).decode()[0:length]

print(generate_password())


```

### Para visualizar el diagrama de flujo, sigue estos pasos:

##### 1. Descarga el archivo draw.io adjunto al proyecto [password.drawio]

##### 2. Abre el archivo draw.io en tu editor de diagramas de flujo preferido (por ejemplo, draw.io Desktop).

##### 3. Haz clic en "Open Existing Diagram" y selecciona el archivo draw.io descargado.

##### 4. El diagrama de flujo se abrirá en tu editor de diagramas de flujo.

### 5. O puedes ingresar al index.html adjunto aqui en el proyecto, y correr el diagrama de forma local en el navegador.

## Datos del estudiante

- **Nombre:** Anggie Alava
- **Materia:** Logica de Programación
- **Carrera:** Ingeniería en Software
- **Semestre:** 1
- **Email de contacto:** analavaes@uide.edu.ec

### Link al Tutorial

⬇️
⬇️
⬇️
⬇️

### [Clic aquí para ver el Tutorial](https://drive.google.com/file/d/1Sp2htA4kbOBadKkUJStNdJi2_sS-MNCy/view?usp=drive_link)
