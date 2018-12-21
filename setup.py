from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="digole",
    version="0.0.3",
    author="John Thornton",
    author_email="bjt128@gmail.com",
    license="MIT License",
    description="Digole LCD Drivers",
    long_description=long_description,
    url="https://github.com/jethornton/digole",
    packages=find_packages('src'),
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    py_modules={'digole'},
    install_requires={'smbus2'},
)
