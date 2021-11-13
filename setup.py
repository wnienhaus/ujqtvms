import re
import os
import sdist_upip
from setuptools import setup


def long_desc_from_readme():
    with open('README.md', 'r') as fd:
        long_description = fd.read()

        return long_description


def get_version():
    return os.environ.get('VERSION', None)


setup(
    name="ujqtvms",
    version=get_version(),
    description="Testing automated pypi publishing vi Github releases",
    long_description=long_desc_from_readme(),
    long_description_content_type='text/markdown',
    url="https://github.com/wnienhaus/ujqtvms",
    license="MIT",
    author="ujqtvms authors",
    author_email="wnienhaus@email.com",
    maintainer="ujqtvms authors",
    maintainer_email="wnienhaus@email.com",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: Implementation :: MicroPython',
    ],
    platforms=["esp32", "linux", "darwin"],
    cmdclass={"sdist": sdist_upip.sdist},
    packages=["ujqtvms"],
    extras_require={"test": ["pytest"]}
)
