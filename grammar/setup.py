#!/usr/bin/env python3
"""
Setup script for Copper ANTLR Python parser
"""

import os
import subprocess
import sys
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py


class BuildPyCommand(build_py):
    """Custom build command to generate ANTLR parser"""
    
    def run(self):
        # Generate Python parser from ANTLR grammar
        self.generate_antlr_parser()
        super().run()
    
    def generate_antlr_parser(self):
        """Generate Python parser using ANTLR4"""
        print("Generating Python parser from ANTLR grammar...")
        
        antlr_dir = os.path.join(os.path.dirname(__file__), 'antlr')
        output_dir = os.path.join(os.path.dirname(__file__), 'build', 'python')
        
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate parser
        cmd = [
            'antlr4',
            '-Dlanguage=Python3',
            '-visitor',
            '-listener',
            '-o', output_dir,
            os.path.join(antlr_dir, 'Copper.g4')
        ]
        
        try:
            subprocess.run(cmd, check=True, cwd=antlr_dir)
            print("✓ Python parser generated successfully")
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to generate Python parser: {e}")
            sys.exit(1)
        except FileNotFoundError:
            print("✗ antlr4 command not found. Please install ANTLR4.")
            print("  Visit: https://github.com/antlr/antlr4/blob/master/doc/getting-started.md")
            sys.exit(1)


def read_requirements():
    """Read requirements from requirements.txt"""
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(requirements_path):
        with open(requirements_path, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return ['antlr4-python3-runtime>=4.13.1']


def read_readme():
    """Read README for long description"""
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "ANTLR4-generated parser for the Copper metadata language"


setup(
    name='copper-antlr-parser',
    version='1.0.0',
    description='ANTLR4-generated parser for the Copper metadata language',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    author='Copper Language Team',
    author_email='team@copper-lang.org',
    url='https://github.com/copper-lang/copper',
    license='MIT',
    
    # Package configuration
    packages=find_packages(),
    package_dir={'': 'build/python'},
    python_requires='>=3.7',
    
    # Dependencies
    install_requires=read_requirements(),
    
    # Entry points
    entry_points={
        'console_scripts': [
            'copper-parse=copper_parser.main:main',
        ],
    },
    
    # Custom build command
    cmdclass={
        'build_py': BuildPyCommand,
    },
    
    # Classification
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Compilers',
        'Topic :: Text Processing :: Linguistic',
    ],
    
    # Additional metadata
    keywords='antlr parser copper metadata dax lookml',
    project_urls={
        'Bug Reports': 'https://github.com/copper-lang/copper/issues',
        'Source': 'https://github.com/copper-lang/copper',
        'Documentation': 'https://docs.copper-lang.org',
    },
)