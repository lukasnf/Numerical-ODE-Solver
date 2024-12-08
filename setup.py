from setuptools import setup, find_packages

classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

setup(
    name= "numODEsolver",
    version= "0.1",
    description= "Tool that solves and plots ODE's numerically. Written in Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lukasnf/Numerical-ODE-Solver",
    packages = find_packages(),
    install_requires=["numpy","matplotlib","sympy","scipy"],
    classifiers=classifiers,
    python_requires=">=3.8",

)