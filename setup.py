import setuptools

with open("README.md", "r") as fh:
        long_description = fh.read()

setuptools.setup(
        name="pyally",
        version="0.2.4",
        author="Brett Graves",
        author_email="alienbrett648@gmail.com",
        description="Ally Invest API Wrapper",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/alienbrett/PyAlly",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
        ],
)
