from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in prestige_app/__init__.py
from prestige_app import __version__ as version

setup(
	name="prestige_app",
	version=version,
	description="This is a custom app for creating new doctypes webforms etc...",
	author="Mohseen Habib",
	author_email="mohseen@dlisaudi.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
