import re
from setuptools import setup, find_packages

with open("diffpriv_laplace/version.py", "r") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

if not version:
    raise RuntimeError("Cannot find version information")

url = "https://github.com/aleph-research/diff-priv-laplace-python"

setup(
    name="diff-priv-laplace-python",
    version=version,
    description="Python library for Laplace differential privacy",
    long_description="",
    keywords="laplace, differential, privacy",
    author="Elmar Langholz",
    author_email="langholz@gmail.com",
    url=url,
    download_url="{}/tarball/v{}".format(url, version),
    license="MIT",
    packages=find_packages(exclude="tests"),
    package_data={"README": ["README.md"]},
    install_requires=["numpy>=1.18.2"],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
