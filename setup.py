from setuptools import setup, find_packages
import sys, os

from manifold.manifold import __version__ as version

setup(name='Manifold',
      version=version,
      description="An SMF service manifest creation tool.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='SMF manifest XML',
      author='Chris Miles',
      author_email='miles.chris@gmail.com',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points = {
          'console_scripts': [
              'manifold = manifold.manifold:main',
          ],
      },
)
