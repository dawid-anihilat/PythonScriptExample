from setuptools import setup, find_packages

with open('README.rst','r') as f:
        readme = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    description="Database backup locally or AWS S3.",
    long_description=readme,
    author="Dawid Adamski",
    author_email='dawid.adamski@atos.net',
    packages=find_packages('src'),
    package_dir={'':'src'},
    install_requires=['boto3'],
    entry_points={
            'console_scripts':  [
                    'pgbackup=pgbackup.cli:main',
                ]
        }
)
