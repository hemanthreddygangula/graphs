from setuptools import setup, find_packages

setup(
    name="my_graphs_package",  # Your package name
    version="0.1.0",  # Initial version
    description="A package for graph algorithms, including Floyd-Warshall.",
    long_description=open("graphs/README.md").read(),
    long_description_content_type="text/markdown",
    author="Hemanth Reddy Gangula",
    author_email="hemanthreddy8181@gmail.com",
    packages=find_packages(),  # Automatically discover the 'graphs' package
    python_requires=">=3.6",  # Specify the minimum Python version
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
