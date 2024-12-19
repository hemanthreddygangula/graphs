from setuptools import setup, find_packages

setup(
    name="floyd_warshall_bidirectional",
    version="0.1.0",
    description="A Function to find the shortest path between the nodes with the given weights/distance between the nodes.",
    author="Hemanth Reddy Gangula",
    author_email="hemanthreddy8181@gmail.com",
    packages=find_packages(),
    install_requires=[],  # Add any dependencies here
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
