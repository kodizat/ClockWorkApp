FROM python:3.11.9
WORKDIR /app  

COPY . .  

EXPOSE 5432

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]  
