import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="osc-utils",
    version="0.1",
    author="Léon Lenclos",
    author_email="leon.lenclos@gmail.com",
    description="Simple command line tools to send or receive OSC messages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license = 'UNLICENSE',
    url="https://github.com/LeonLenclos/osc-utils",
    keywords = [
        'osc',
    ],
    packages=['oscutils'],
    entry_points={
        'console_scripts': [
            'osc-client=oscutils.interactive:client',
            'osc-server=oscutils.interactive:server',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=['color', 'python-osc']
)