import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_easy_metatags", # Replace with your own username
    version="0.2",
    author="Hardeep Singh",
    author_email="hardeep0khalsa122@gmail.com",
    description="A Django app to add meta tags to any page of your website.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hardeepsingh980/django_simple_metatags",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)