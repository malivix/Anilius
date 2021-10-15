import io
import re
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with io.open("src/anilius/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setuptools.setup(
    name="Anilius",
    version=version,
    description="A high performance grpc micro framework based on python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Malivix/Anilius",
    author="Mahdi Zarrintareh",
    author_email="mza2rintareh@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    python_requires=">=3.0",
    entry_points={"console_scripts": ["anilius = anilius.cli.main:main"]},
)
