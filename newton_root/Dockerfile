FROm alpine:latest

RUN apk add --no-cache bash
RUN apk add --no-cache python3

ADD . app

ENTRYPOINT ["python3", "app/newton_root.py"]
CMD []
