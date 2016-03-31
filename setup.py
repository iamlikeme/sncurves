from distutils.core import setup

LICENSE = open("LICENSE").read()
LONG_DESCRIPTION = open("README.md").read()    

setup(name='sncurves',
      version='1.0',
      author='Piotr Janiszewski',
      author_email='i.am.like.me@gmail.com',
      url='https://github.com/iamlikeme/sncurves/',
      description='Python implementation of the DNV S-N curves for fatigue analysis',
      long_description=LONG_DESCRIPTION,
      license=LICENSE,
      py_modules=['sncurves'],
     )
