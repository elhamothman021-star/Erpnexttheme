# ---------------------------------------------------------------------------
# YOU Telecom | Enterprise Digital Transformation
# edt_ui - Shared UI Foundation / Design System
# 
# Author   : Anwar Taha Mohammed Al-Hitar
# Role     : Applications Developer Specialist - 2H | CEO Office
# Contact  : eyaalhitar@you.com.ye
# Created  : October 2026
# Version  : 20261021f
# ---------------------------------------------------------------------------

from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="edt_ui",
    version="1.0.0",
    description="Enterprise Digital Transformation UI - Shared UI Foundation / Design System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Anwar Taha Mohammed Al-Hitar",
    author_email="eyaalhitar@you.com.ye",
    maintainer="YOU - Head Office",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=["frappe"],
    classifiers=[
        "Framework :: Frappe",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
