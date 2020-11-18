from setuptools import setup, find_packages

packages = find_packages(
    where='.',
    include=['pyjeasy*']
)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyjeasy",
    version="0.1.0",
    author="Jitesh Gosar",
    author_email="gosar95@gmail.com",
    description="Useful python tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jitesh17/pyjeasy",
    py_modules=["pyjeasy"],
    packages=packages,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'printj',
        'opencv-python',
        'numpy',
        'matplotlib',
        'pandas',
        # 'math',

    ],
    python_requires='>=3.6',
)
