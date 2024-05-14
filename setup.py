import setuptools

setuptools.setup(
    name="qc-library",
    version="0.1.0",
    description="A quantum computing library",
    author="KOSASIH",
    author_email="kosasihg88@gmail.com",
    url="https://github.com/KOSASIH/qc-library",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy",
        "qiskit"
    ],
    entry_points={
        "console_scripts": [
            "qc = qc_library.__main__:main"
        ]
    },
    python_requires=">=3.7"
)
