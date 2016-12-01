FROM phusion/baseimage:0.9.19

RUN rm -f /etc/service/sshd/down
EXPOSE 8010

ADD key.pub /tmp/key.pub
ADD requirements/dev.txt requirements.txt
RUN cat /tmp/key.pub >> /root/.ssh/authorized_keys && rm /tmp/key.pub
RUN apt-get update
RUN apt-get install -y python-pip
RUN ls -l .
ADD requirements/ requirements/
RUN pip install -r requirements/dev.txt