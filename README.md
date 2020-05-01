# docker-tcp-udp-listener


Docker image that listens on a specified UDP port, outputs to container log.

### Start it

By default, you can run it like this

    docker run -p 0.0.0.0:5000:5000 -p 0.0.0.0:5000:5000/tcp -p 0.0.0.0:5005:5005 -p 0.0.0.0:5005:5005/udp --name udp-listener hello2parikshit/docker-tcp-udp-listener

You can make it listen on another port

    docker run -p 0.0.0.0:4000:4000 -p 0.0.0.0:4000:4000/tcp -p 0.0.0.0:4004:4004 -p 0.0.0.0:4004:4004/udp --name udp-listener hello2parikshit/docker-tcp-udp-listener

#### Test it for UDP

In another terminal:

    nc -u localhost 5005

    nc -u localhost 4004

### Test it for TCP 
 Run client to test TCP connection in another terminal:

    python tcpclient.py <serverip/hostname> <port>

And start sending data.  You should see your text reflected in the `docker run` terminal


### Docker Compose

```
tcpudp:
  container_name: my-tcp-udp-listener
  image: hello2parikshit/docker-tcp-udp-listener
  environment:
    - UDPPORT=4004
    - TCPPORT=4000
  ports:
  - "0.0.0.0:4000:4000"
  - "0.0.0.0:4000:4000/tcp"
  - "0.0.0.0:4001:4004"
  - "0.0.0.0:4001:4004/udp"

```

View its logs:

    docker logs my-tcp-udp-listener


Ref : https://pymotw.com/2/socket/tcp.html