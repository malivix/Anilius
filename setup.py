import io
import re

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("src/anilius/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="Anilius",
    version=version,
    description="GRPC framework for microservice ecosystem",
    long_description=readme,
    author="Mahdi Zarrintareh",
    author_email="mza2rintareh@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        "alembic>=1.3.2",
        "black>=18.9b0",
        "coverage>=5.*",
        "flake8>=3.7.*",
        "grpcio>=1.26.*",
        "grpcio-tools>=1.26.*",
        "mysqlclient>=1.4.6",
        "passlib>=1.7.2",
        "phonenumbers>=8.11.1",
        "pytest>=5.3.4",
        "pytest-cov>=2.8.1",
        "pytest-xdist>=1.31.0",
        "PyJWT>=1.7.1",
        "py-grpc-prometheus>=0.2.0",
        "sentry-sdk>=0.14.1",
        "SQLAlchemy>=1.3.12",
        "SQLAlchemy-Utils>=0.36.1",
        "zimports>=0.2.0",
    ],
    extras_require={"dotenv": ["python-dotenv"], "dev": ["pytest", "coverage", "tox"]},
    entry_points={"console_scripts": ["anilius = anilius.cli.main:main"]},
)
