from setuptools import setup,find_packages

setup(
    name = 'websocket_server',
    version = '0.4',
    packages = find_packages("."),
    url = 'https://github.com/Pithikos/python-websocket-server',
    liences = 'MIT',
    author = 'orangehaswing',
    author_email = '673556024@qq.com',
    install_requires = [
    ],
    description = 'A simple fully working websocket-server in Python with no external dependencies',
    platforms = 'any',
)