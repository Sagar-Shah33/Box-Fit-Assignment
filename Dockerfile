# FROM python:3.8.6-alpine3.12
FROM python:3.8.6-alpine

# define present working directory
WORKDIR /Box_Docker

# copy the contents into the working dir
ADD . /Box_Docker

# Run pip to install dependencies of the flask
RUN pip install -r requirements.txt

# Define the command to start the container
CMD [ "python", "test.py" ]

# EXPOSE 5000


# COPY ./app ./app
# COPY requirements.txt .

# RUN pip install -r requirements.txt 


# ENTRYPOINT [ "flask" ]
# CMD [ "./app/test.py", "--host", "0.0.0.0" ]