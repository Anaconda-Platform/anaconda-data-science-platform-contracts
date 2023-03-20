import setuptools

setuptools.setup(
    name="anaconda.enterprise.server.contracts",
    version="0.11.0",
    package_dir={"": "src"},
    packages=setuptools.find_namespace_packages(where="src"),
    author="Joshua C. Burt",
    description="Anaconda Enterprise Server Contracts",
    long_description="Anaconda Enterprise Server Contracts",
    include_package_data=True,
    zip_safe=False,
)
