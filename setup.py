#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="textfsm_iij_seil",
    version="0.1",
    author="Ruy",
    author_email="ruy(at)ainoniwa.net",
    url="https://github.com/ainoniwa/textfsm_iij_seil",
    description="textfsm_iij_seil: TextFSM template for IIJ SEIL series",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Networking",
    ],
    install_requires=["textfsm"],
    extras_require={"dev": ["pytest", "tox"]},
    packages=find_packages(exclude=['tests']),
    package_data={"textfsm_iij_seil": ["templates/*"]},
)
