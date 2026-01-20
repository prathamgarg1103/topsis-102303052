from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Topsis-Pratham-102303052",
    version="1.0.1",
    author="Pratham",
    author_email="pgarg7_be23@thapar.edu",
    description="A python package for implementing TOPSIS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis_pratham_102303052.topsis:main",
        ],
    },
)
