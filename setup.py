from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dynamic_uom_conversion/__init__.py
from dynamic_uom_conversion import __version__ as version

setup(
	name="dynamic_uom_conversion",
	version=version,
	description="Dynamic Uom Conversion",
	author="Ascra Technologies",
	author_email="nirali@ascratech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
