from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="volk",
    version="0.0.4",
    description="WSGI Server",
    packages=["volk"],
    py_modules=["volk"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "volk = volk.__main__:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joegasewicz/volk",
    author="joegasewicz",
    author_email="contact@josef.digital",
)
