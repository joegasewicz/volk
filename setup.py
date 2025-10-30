import os

from pygments.lexers.sql import language_re
from setuptools import setup, Extension
from Cython.Build import cythonize

here = os.path.abspath(os.path.dirname(__file__))

ext = Extension(
    name="volk._volk",
    sources=[
        "volk/volk.pyx",
        "volk.c",
    ],
    include_dirs=[here],
    extra_compile_args=[],
    extra_link_args=[],
    language="c",
)

setup(
    name="volk",
    version="0.0.1",
    description="Python bindings for volk C library",
    packages=["volk"],
    package_data={"volk": ["*.pxd", "*.pyx", "py.typed"]},
    ext_modules=cythonize([ext], language_level=3),
)
