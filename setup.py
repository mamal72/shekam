from setuptools import setup

setup(
    name='shekam', version='0.1.0',
    description='Shekam is an API based of Hazm',
    author='Mohamad Jahani',
    author_email='m4m4lj@gmail.com',
    url='https://github.com/mamal72/shekam',
    test_suite="tests",
    install_requires=[
        'aiofiles==0.3.0',
        'hazm==0.5.2',
        'httptools==0.0.9',
        'libwapiti==0.2.1',
        'multidict==2.1.4',
        'nltk==3.0.5',
        'requests==2.12.5',
        'Sanic==0.2.0',
        'six==1.10.0',
        'ujson==1.35',
        'uvloop==0.7.2'
    ]
)
