import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="termchart",
    version="0.0.4",
    author="@JeffProd",
    author_email="termchart@jeffprod.com",
    description="A tool to draw ascii line chart in terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='terminal line chart graph',
    url="https://github.com/Tazeg/termchart",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        'Funding': 'https://en.jeffprod.com/donate/',
        'Twitter': 'https://twitter.com/jeffprod',
        'Web': 'https://jeffprod.com'
    },
)