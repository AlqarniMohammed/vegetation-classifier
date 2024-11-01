from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='vegatation',
      version="0.0.1",
      description="Vegatation classefier Model for cover type",
      license="MIT",
      author="vegatation-classefier",
      author_email="mosalehalqarni@gmail.com",
      install_requires=requirements,
      packages=find_packages(),
      test_suite="tests",
      include_package_data=True,
      zip_safe=False)
