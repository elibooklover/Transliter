from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(name='transliter',
    python_requires='>=3.6',
    version='0.3.7',
    url='https://github.com/elibooklover/Transliter',
    license='GPL-2.0',
    author='Hoyeol Kim',
    author_email='elibooklover@gmail.com',
    description='TransLiter transliterates multilingual text into Latin script.',
    packages=['transliter', ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "pandas",
        "pykakasi"
    ]
)