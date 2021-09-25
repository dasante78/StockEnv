# Copyright 2019 by Daniel Prakah-Asante
# All rights reserved.
# This file is part of the StockEnv package,
# and is released under the "GNU  General Public License v3.0". Please see the LICENSE
# file that should have been included as part of this package.
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
from setuptools import setup
setup(
  name = 'StockEnv',        
  packages = ['StockEnv'],  
  version = '0.0.10',     
  license='GNU GPLv3',        
  description = 'Stock environment for training machine learning agents',  
  author = 'Daniel Prakah-Asante',                  
  author_email = 'dprakahasante@gmail.com',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url = 'https://github.com/user/dasante78',   
  download_url = 'https://github.com/dasante78/StockEnv/archive/v_009.tar.gz',    
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
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',   
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
