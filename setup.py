from setuptools import setup, find_packages

setup(
    name="carbonswipe",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        # e.g. "codecarbon>=2.1.4",
    ],
    author="Jasraj Budigam",
    description="Measure energy, CO2 & water use of local LLM inference",
    url="https://github.com/rajbudigam/CarbonSwipe",
    python_requires=">=3.7",
)
