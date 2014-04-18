from setuptools import setup, find_packages

setup(
    name = "django_payone",
    version = "0.1.0-3",
    description = 'Payone client and server API',
    author = 'David Danier',
    author_email = 'david.danier@team23.de',
    url = 'https://github.com/ddanier/django_payone',
    long_description=open('README.rst', 'r').read(),
    packages = [
        'django_payone',
        'django_payone.channel',
    ],
    package_data = {
        'django_payone': ['static/payone/client.js'],
    },
    install_requires = [
        'Django >=1.3',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)

