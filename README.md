# sqslistener
AWS SQS Listener

## install:

- clone repo
- cd into repo root
- install service module `pip install service`
- run `python setup.py install`

## usage:
make sure that you have the main AWS environment variable set: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_DEFAULT_REGION`

```
sqslistener <SQS_URL> <FILE_PATH> <COMMAND (start/stop/status)>
```
