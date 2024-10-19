from pathlib import Path

from setuptools import find_packages, setup

readme_file = Path(__file__).parent / "README.md"
with readme_file.open() as f:
    long_description = f.read()

setup(
    name="isic-metadata",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache 2.0",
    url="https://github.com/ImageMarkup/isic-metadata",
    project_urls={
        "Bug Reports": "https://github.com/ImageMarkup/isic-metadata/issues",
        "Source": "https://github.com/ImageMarkup/isic-metadata",
    },
    author="Kitware, Inc.",
    author_email="kitware@kitware.com",
    keywords="requests",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python",
    ],
    python_requires=">=3.10",
    install_requires=["pydantic>=2.4"],
    extras_require={
        "test": [
            "coverage[toml]",
            "hypothesis",
            "pytest",
            "pytest-mock",
            "pytest-cov",
        ],
    },
    packages=find_packages(),
    # needed to py.typed
    include_package_data=True,
)
