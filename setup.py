from setuptools import setup, find_packages
import os
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.1.1'
DESCRIPTION = 'Stock environment for training machine learning agents'

# Setting up
setup(
    name="stocktrainer",
    version=VERSION,
    author="Daniel Prakah-Asante",
    author_email="doprakah@mit.edu",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
     packages=find_packages(),
     url='https://github.com/dasante78/StockTrainer',  
     keywords = ['USEFULL', 'STOCKS','MACHINE LEARNING', 'AI', 'ARTIFICAL INTELLIGENCE' ],   
  install_requires=[           
          'pandas',
          'numpy',
          'datetime',
          'pandas_datareader',
          'yfinance'
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
