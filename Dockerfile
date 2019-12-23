FROM python:3.6.10-alpine
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
    && apk update \
    && apk add git gcc musl-dev libffi-dev openssl-dev make
COPY . /data/app/http_server
WORKDIR /data/app/http_server
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt \
&& chmod +x run.sh
EXPOSE 5001
CMD ["sh", "/data/app/http_server/run.sh"]
