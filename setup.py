from setuptools import setup

setup(
    name='sqslistener',
    version='0.1',
    packages=['sqslistener'],
    url='https://github.com/Sikilabs/sqslistener',
    license='MIT',
    author='Ibrahim Diop',
    author_email='ibrahim@sikilabs.com',
    description='AWS SQS Listener',
    install_requires=[
        "service",
        "boto3"
    ],
    entry_points={
        'console_scripts': [
            'sqslistener = sqslistener.__main__:go'
        ]
    }
)
