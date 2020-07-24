import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='rem-calc',
    version='1.0',
    author='KurzGedanke',
    author_email="rem_calc@kurzgedanke.me",
    license='MIT',
    keywords='rem css webdev',
    description="rem-calc helps you to calculate rem values based on pixel values.",
    url='https://github.com/KurzGedanke/rem-calc',
    download_url='https://github.com/KurzGedanke/rem-calc/archive/v1.0.0.tar.gz',
    long_description=read('README.md'),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'rem-calc = rem_calc.rem_calc:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
