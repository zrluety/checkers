from setuptools import setup, find_packages

install_requires = ["pandas"]

setup(
    name="checkers",
    version="0.0.2",
    packages=find_packages(exclude=["tests"]),
    install_requires=install_requires,
    author="Zachary Luety",
    author_email="zluety@gpwa.com",
    description="Quickly check data with Python",
)
