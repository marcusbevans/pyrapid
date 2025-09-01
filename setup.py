import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyrapid',
    version='1.0.0',
    author='Marcus Evans',
    author_email='marcus@marcusbevans.com',
    description='Python client library for Rapid Response Management System (RRMS) API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/marcusbevans/pyrapid',
    project_urls={
        "Bug Tracker": "https://github.com/marcusbevans/pyrapid/issues",
        "Documentation": "https://github.com/marcusbevans/pyrapid#readme",
        "Source Code": "https://github.com/marcusbevans/pyrapid"
    },
    license='MIT',
    packages=setuptools.find_packages(exclude=['tests*', 'examples*']),
    install_requires=[
        'requests>=2.25.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
        ],
        'examples': [
            'python-dotenv>=0.19.0',
            'pandas>=1.3.0',
        ],
    },
    python_requires='>=3.7',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
    ],
    keywords='rapid response rrms api client rest',
)
