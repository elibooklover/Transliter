from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(name='TransLiter',
    python_requires='>=3.6',
    version='0.2.5',
    url='https://github.com/elibooklover/TransLiter',
    license='MIT',
    author='Hoyeol Kim',
    author_email='elibooklover@gmail.com',
    description='TransLiter transliterates multilingual text into English.',
    packages=['TransLiter', ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "pandas",
        "pykakasi"
    ]
)