# imagen de python
FROM python:3.12-slim

# evita que Python genere archivos .pyc y permite ver logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# directorio de trabajo
WORKDIR /app

# depencias para que el sistema entienda postgre
RUN apt-get update && apt-get install -y libpq-dev gcc

# copiamos dependencias de librerias y las instalamos
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código del proyecto
COPY . /app/