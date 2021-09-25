from setuptools import setup, find_packages
import os

VERSION = '0.0.1'
DESCRIPTION = 'Stock environment for training machine learning agents'

# Setting up
setup(
    name="StockEnv",
    version=VERSION,
    author="Daniel Prakah-Asante",
    author_email="doprakah@mit.edu",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
     keywords = ['USEFULL', 'STOCKS','MACHINE LEARNING', 'AI', 'ARTIFICAL INTELLIGENCE' ],   
  install_requires=[           
          'pandas',
          'numpy',
          'datetime',
          'pandas_datareader'
      ],
        classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',    
    'Topic :: Software Development :: Build Tools',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ]
)
