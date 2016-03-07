
from setuptools import setup, find_packages
from os.path import join, dirname

try:
    f = open(join(dirname(__file__), 'README.rst'))
    long_description = f.read().strip()
    f.close()
except IOError:
    long_description = None

setup(
    name			='django-brokenlinks',
    version			='0.1.0',
    url				='https://github.com/wtayyeb/django-brokenlinks',
    description		='reusable django app to log crawlers hitting many 404 pages.',
    long_description=long_description,
    author			='wtayyeb',
    author_email	='wtayyeb@gmail.com',
    license			='MIT',
    keywords		='django brokenlinks',
    platforms		='any',
    classifiers		=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages		=find_packages(),
	install_requires=['django-appconf', ],
)
