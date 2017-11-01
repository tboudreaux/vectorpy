from setuptools import setup
from os import path

HERE = path.abspath(path.dirname(__file__))

setup(name='vectorpy',
      version='1.4',
      description='Basic 3 Vector Object',
      url='https://github.com/tboudreaux/vectorpy.git',
      author='Thomas Boudreaux',
      author_email='thomas@boudreauxmail.com',
      license='MIT',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3'
      ],
      install_requires=[
          'numpy>=1.12.0'
      ],
      packages=['vectorpy'],
      zip_safe=False)
