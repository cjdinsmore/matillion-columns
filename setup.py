import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="generate-matillion-columns",
    version="0.0.1",
    author="Caleb Dinsmore",
    author_email="caleb.dinsmore@edusource.us",
    description="A tool to generate columns in our Matillion grid variables using CSVs on S3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    entry_points={
        'console_scripts': ['matillion-columns=matillion_columns.command_line:main']
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)