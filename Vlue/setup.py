import setuptools

setuptools.setup(
    name="Vlue",
    version="0.1.0",
    license = "MIT",
    author="jhlee838",
    author_email="jhlee@xzx.kr",
    description="Programming language",
    long_description=open('../readme.md').read(),
    url="https://github.com/jhlee838/blue-lang",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    scripts=['']
)