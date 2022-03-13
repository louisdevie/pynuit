import sys

from setuptools import setup
from setuptools_rust import RustExtension

with open("README.md", "rt") as fd:
    README = fd.read()

setup(
    name="pynuit",
    version="0.0.1",
    license="MIT",
    author="Louis DEVIE",
    author_email="louisdevie.contact@gmail.com",
    url="https://github.com/louisdevie/minuitpy",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=["pynuit"],
    install_requires="setuptools-rust>=0.12.1",
    python_requires=">=3.8",
    rust_extensions=[RustExtension("pynuit.minuit_py")],
)
