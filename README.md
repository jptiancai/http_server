# HTTP_SERVER
A target test tttp server.

## pull python docker

```
docker pull python:3.6.10-alpine
```

## build docker
```
docker build -t http_server:http_server .
```

## run docker
```
docker run -d -v /tmp/http_logs:/data/app/http_server/logs -p 5001:5001 http_server:http_server
```