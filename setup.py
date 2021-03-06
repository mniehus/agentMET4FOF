# -*- coding: utf-8 -*-
"""
Install agentMET4FOF in Python path.
"""

import os
import sys

from setuptools import setup, find_packages
from setuptools.command.install import install

# Get release version from agentMET4FOF/__init__.py
from agentMET4FOF import __version__ as VERSION


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def readme():
    """Print long description"""
    with open("README.md") as f:
        return f.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""

    description = "Verify that the git tag matches our version"

    def run(self):
        tag = os.getenv("CIRCLE_TAG")

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: " "{1}".format(
                tag, VERSION
            )
            sys.exit(info)


setup(
    name="agentMET4FOF",
    version=VERSION,
    description="A software package for the integration of metrological input "
    "into an agent-based system for the consideration of measurement "
    "uncertainty in current industrial manufacturing processes.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/bangxiangyong/agentMET4FOF",
    author=u"Bang Xiang Yong, Björn Ludwig, Haris Lulic",
    author_email="bxy20@cam.ac.uk",
    keywords="uncertainty metrology MAS agent-based agents",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "ipykernel",
        "numpy",
        "scikit-learn",
        "scikit-multiflow",
        "scipy",
        "matplotlib",
        "pandas",
        "seaborn",
        "osbrain",
        "dash",
        "dash-cytoscape",
        "networkx",
        "multiprocess",
        "h5py",
        "requests",
        "plotly",
    ],
    python_requires=">=3",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python :: 3",
    ],
    cmdclass={"verify": VerifyVersionCommand,},
)
