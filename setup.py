import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dic_academic_api",
    version='0.0.2',
    author="drforse",
    author_email="george.lifeslice@gmail.com",
    description="A package for direct acessing to dic_academic api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drforse/dic_academic_api",
    install_requires=['requests'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)