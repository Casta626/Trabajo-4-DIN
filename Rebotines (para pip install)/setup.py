import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rebotines",
    version="0.1",
    author="José Antonio Castañeda Pavón",
    author_email="joseantoniocastanedapavon@gmail.com",
    description="Librería que crea un componente que va rebotando por la pantalla",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Casta626/Trabajo-4-DIN",
    project_urls={
        "Repo": "https://github.com/Casta626",
    },
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.10",
)