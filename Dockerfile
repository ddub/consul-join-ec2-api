FROM tatsushid/tinycore-python:3.5
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
RUN chmod 755 /usr/src/app/*.py
ENTRYPOINT [ "/usr/src/app/consul-join-ec2-api.py" ]
