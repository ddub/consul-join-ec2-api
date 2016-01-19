FROM python:3-onbuild
RUN chmod 755 *.py
ENTRYPOINT [ "/usr/src/app/show-ips-for-asg.py" ]
