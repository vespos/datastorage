from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='datastorage',
      version='0.1',
      description='Dict-like object that can be saved in hdf5 or numpy format',
      long_description=readme(),
      url='https://git.ipr.univ-rennes1.fr/mcammara/datastorage',
      author='marco cammarata',
      author_email='marco.cammarata.xray@gmail.com',
      license='MIT',
      packages=['datastorage'],
      install_requires=[
          'numpy',
          'h5py',
      ],
      zip_safe=False)