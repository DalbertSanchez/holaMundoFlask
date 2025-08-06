# Imagen base oficial de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos al contenedor
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Exponer el puerto que usará la app
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]
