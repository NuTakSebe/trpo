FROM ubuntu:latest
MAINTAINER Egor Kashirin "mailgorinich@gmail.com"
RUN apt-get update -y && apt-get install -y python3-pip python3-dev build-essential locales
RUN pip3 install flask
# Copy working directory
COPY . /app
WORKDIR /app
# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
# Commands after container was created
CMD ["export", "FLASK_APP=app.py"]
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
