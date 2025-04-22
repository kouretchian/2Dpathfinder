from setuptools import setup, find_packages

setup(
    name="pathfinder2d",
    version="0.1.0",
    author="Mahdi Kouretchian",
    description="2D Path Finding in Binary Images using Black Pixels",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["numpy>=1.23", "imageio>=2.31", "matplotlib>=3.7", "pyyaml>=6.0"],
    extras_require={"dev": ["pytest>=7.2", "mypy>=1.5"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    include_package_data=True,
    entry_points={"console_scripts": ["pathfinder2d=main:main"]},
)
