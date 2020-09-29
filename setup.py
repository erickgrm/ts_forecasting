import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="forecasts-erickgrm", # Replace with your own username
    version="0.0.1",
    author="github.com/erickgrm",
    author_email="erick.grmr@gmail.com",
    description="Forecasting of time series",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/erickgrm/ts_forecasting",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
