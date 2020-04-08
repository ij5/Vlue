from distutils.core import setup, Extension

setup(name="ezthon",
      version="1.0",
      description="simple python package.",
      author="Jaehee Lee",
      author_email="jhlee838@gmail.com",
      url="ahlir.com",
      ext_modules=[Extension("ezthon",["ezthon.c"])]
      )