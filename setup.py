from setuptools import setup, find_packages

setup(
    name='rem-calc',
    version='1.0',
    author='KurzGedanke',
    author_email="rem_calc@kurzgedanke.me",
    license='MIT',
    keywords='rem css webdev',
    url='https://github.com/KurzGedanke/rem-calc',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'rem-calc = rem_calc.rem_calc:main'
        ]
    }
)