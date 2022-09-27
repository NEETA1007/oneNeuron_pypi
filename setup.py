import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
PROJECT_NAME = "oneNeuron_pypi"
USER_NAME = "NEETA1007"

setuptools.setup(
    name=f"{PROJECT_NAME}-{USER_NAME}",
    version = "0.0.1",
    authors = USER_NAME,
    author = USER_NAME,
    author_email="neeta.aero@gmail.com",
    description = "Its implementation of Perceptron",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[
        "numpy",
        "tqdm"
    ]
)