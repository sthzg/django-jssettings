import os
from distutils.core import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-jssettings',
    version='0.0.1',
    url='',
    packages=['jssettings'],
    license='MIT',
    author='Stephan Herzog',
    author_email='sthzg@gmx.net',
    description='Populate a javascript data object from Django.',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
