
FROM python:3.9
 
COPY . /app
WORKDIR /app
 
RUN pip install -r reqiurement.txt
EXPOSE 6000
 
CMD ["python3", "main.py"]