from setuptools import setup, find_packages

setup(
    name="my_sugar",               # package name on PyPI
    version="0.1",
    author="Natee",
    author_email="33nateejunrungsee@lannaist.ac.th",
    description="Mini Python shorthand library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SuperHappyCat/sugar_module",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
