import setuptools

# Read the dependencies from requirements.txt
with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')
setuptools.setup(
    name="pytorch_cifar10",
    version="0.0.1",
    packages=setuptools.find_packages(), 
    install_requires=install_requires
)
