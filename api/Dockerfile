FROM python
WORKDIR /flask-app

#Comando para instalação do "requirements.txt"
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python3 -m pip install -r requirements.txt

EXPOSE 5000
COPY . .
# Run the application.
CMD python3 -m flask --app __init__ run --host=0.0.0.0