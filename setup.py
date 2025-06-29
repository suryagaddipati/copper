from setuptools import setup, find_packages

setup(
    name="copper",
    version="0.1.0",
    description="Universal Semantic Layer - Define Once. Run Anywhere.",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "antlr4-python3-runtime>=4.9.0",
        "pyyaml>=6.0",
        "pandas>=1.3.0",
        "pydantic>=1.8.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "mypy>=0.910",
        ],
        "spark": ["pyspark>=3.0.0"],
        "beam": ["apache-beam>=2.0.0"],
    },
    entry_points={
        "console_scripts": [
            "copper=copper.cli:main",
        ],
    },
)