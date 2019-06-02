import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, "README.md")) as f:
    README = f.read()

URL = "https://github.com/vincentzhchen/audiotagger"

setup(
    name="audiotagger",
    version="0.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pandas>=0.18.0,<0.24.0",
                      "mutagen>=1.41.1",
                      "redquill"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest-cov"],
    python_requires=">=3.6",

    # metadata to display on PyPI
    license="GPL-3.0-or-later",
    description="Cross-platform metadata editor for audio files.",
    long_description=README,
    long_description_content_type="text/markdown",

    author="Vincent Chen",
    author_email="vincent.zh.chen@gmail.com",
    url=URL,
    project_urls={
        "Source": URL
    },
    classifiers=[
        "License :: OSI Approved :: "
        "GNU General Public License v3 or later (GPLv3+)",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: System :: Logging",
    ],
)
