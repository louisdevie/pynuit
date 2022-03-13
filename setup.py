import sys

from setuptools import setup
from setuptools_rust import RustExtension

with open("README.md", "rt") as fd:
    README = fd.read()

setup(
    name="minuit",
    version="0.0.1",
    license="MIT",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=["minuit"],
    setup_requires="setuptools-rust>=0.12.1",
    python_requires=">=3.8",
    rust_extensions=[RustExtension("minuit.minuit_py")],
)
