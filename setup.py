from setuptools import setup, find_packages
setup(
    name='crime_test', # Package name
    version='1.0', # Package version
    packages=find_packages(), # Automatically find modules
    install_requires=["numpy==2.1.3", "pandas==2.2.3", "python-dateutil==2.9.0.post0", "pytz==2024.2", "setuptools==75.6.0", "six==1.16.0", "tzdata==2024.2"], # Dependencies, if any
    description='Crime Data function package', # Short description
    author='Daniel Chang',
    author_email='daniel.y.chang@sjsu.edu',
)