import logging
import os
import sys
from logging.handlers import SysLogHandler
from service import find_syslog, Service
import boto3


class Listener(Service):
    def __init__(self, *args, **kwargs):
        super(Listener, self).__init__(*args, **kwargs)
        self.logger.addHandler(SysLogHandler(address=find_syslog(),
                                             facility=SysLogHandler.LOG_DAEMON))
        self.logger.setLevel(logging.INFO)

    def run(self):
        sqs = boto3.client('sqs')
        queue_url = os.environ["SQSL_QUEUE_URL"]
        while not self.got_sigterm():
            response = sqs.receive_message(QueueUrl=queue_url)
            try:
                message = response['Messages'][0]
                with open(os.environ["SQSL_FILE_PATH"], "a") as myfile:
                    myfile.write(message)
                receipt_handle = message['ReceiptHandle']
                sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
            except KeyError:
                pass


def go():
    if len(sys.argv) != 4:
        sys.exit('Syntax: %s SQS_URL FILE_PATH COMMAND' % sys.argv[0])

    cmd = sys.argv[3].lower()
    service = Listener('sqs_listener', pid_dir='/tmp')

    os.environ["SQSL_QUEUE_URL"] = sys.argv[1]
    os.environ["SQSL_FILE_PATH"] = sys.argv[2]

    if cmd == 'start':
        service.start()
    elif cmd == 'stop':
        service.stop()
    elif cmd == 'status':
        if service.is_running():
            print("sqs_listener is running.")
        else:
            print("sqs_listener is not running.")
    else:
        sys.exit('Unknown command "%s".' % cmd)

if __name__ == '__main__':
    go()
