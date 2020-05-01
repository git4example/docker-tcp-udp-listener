FROM alpine

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*

RUN pip install --upgrade pip

ENV UDPPORT 5005
ENV TCPPORT 5000

ADD tcpudplistener.py /tcpudplistener.py
ADD tcpclient.py /tcpclient.py
CMD ["python", "-u","/tcpudplistener.py"]

EXPOSE ${UDPPORT}
EXPOSE ${UDPPORT}/udp

EXPOSE ${TCPPORT}
EXPOSE ${TCPPORT}/tcp