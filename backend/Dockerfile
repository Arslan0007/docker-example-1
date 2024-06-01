FROM python:3

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

COPY . .

EXPOSE 8000/tcp

CMD ["fastapi", "dev", "--host=0.0.0.0","main.py"]
