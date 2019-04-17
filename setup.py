import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="inject-globals",
    version="1.0.0",
    author="Victor Williams Stafusa da Silva",
    author_email="victorwssilva@gmail.com",
    description="A decorator for injecting global variables into function calls.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/victorwss/inject-globals",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)