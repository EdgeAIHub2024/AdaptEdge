from setuptools import setup, find_packages

setup(
    name="adaptedge",
    version="0.3.0",
    packages=find_packages(),
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "adaptedge = adaptedge.cli:cli"
        ]
    }
)