from setuptools import setup, find_packages

setup(
    name='itinerary-generator',
    version='0.1.0',
    author='ADev',
    author_email='adev3.14159@gmail.com',
    description='An AI powered itinerary generator.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ADev/itinerary-generator',
    packages=find_packages(),
    install_requires=[
        'cohere>=2.0.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.7',
)
