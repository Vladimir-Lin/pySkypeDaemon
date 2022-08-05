# -*- coding: utf-8 -*-
##############################################################################
from distutils . core import setup
from setuptools       import find_packages
##############################################################################
with open ( "README.rst" , "r" ) as f                                        :
  long_description = f . read (                                              )
##############################################################################
setup ( name='pySkypeDaemon',  # 包名
        version='1.0.0',  # 版本號
        description='Skype Daemon Base on SkPy',
        long_description=long_description,
        author='foxman',
        author_email='lin.vladimir@gmail.com',
        url='https://mp.weixin.qq.com/s/9FQ-Tun5FbpBepBAsdY62w',
        install_requires=[],
        license='BSD License',
        packages=find_packages(),
        platforms=["all"],
        classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries'
        ] ,
)
##############################################################################
