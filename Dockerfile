FROM python:3.11.1

WORKDIR /usr/src/app

COPY . .
RUN pip install --upgrade -r requirements.txt

ENTRYPOINT [ "python3", "./passwd_gen.py" ]