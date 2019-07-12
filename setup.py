from setuptools import setup

with open("README.md", "r") as rm:
    long_description = rm.read()

setup(
    name='slitherlib',
    version='0.1.4',
    description='A web-proxy IP and user agent anonymizing framework for web scrapers, penetration testers, and ethical hackers',
    url='https://github.com/kaelscion/slither',
    author="Jake Cahill",
    author_email="kaelscion@gmail.com",
    license="MIT",
    classifiers=['Intended Audience :: Developers', 'Programming Language :: Python :: 3'],
    packages=['slitherlib', 'slitherlib.proxy', 'slitherlib.user_agent'],
    install_requires=['requests', 'bs4'],
    long_description = long_description,
    long_description_content_type='text/markdown'
)