import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="digole",
    version="0.0.1",
    author="John Thornton",
    author_email="bjt128@gmail.com",
    description="Digole LCD Drivers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jethornton/digole",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
