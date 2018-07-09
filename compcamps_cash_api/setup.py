import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CompCamps-Cash-Api",
    version="1.0.0",
    author="Taylor Petrychyn",
    author_email="compcamps@gmail.com",
    description="A Computer Camp Cryptocurrency API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/compcamps/py-blockchain",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)