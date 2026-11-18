from setuptools import setup, find_packages

classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Operating System :: OS Independent",
]

setup(
    name="numODEsolver",
    version= "3.0",
    description= "Tool that solves ODE's numerically. Written in Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lukasnf/Numerical-ODE-Solver",
    license="MIT",
    packages = ["numODEsolver"],
    install_requires=["numpy","asteval","scipy"],
    classifiers=classifiers,
    python_requires=">=3.8",

)