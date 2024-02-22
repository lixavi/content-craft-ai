from setuptools import setup, find_packages

setup(
    name='contentcraftai',
    version='0.1',
    author='Your Name',
    author_email='your.email@example.com',
    description='AI-driven content generation platform using T5 model',
    long_description='ContentCraftAI is an AI-driven content generation platform that utilizes the T5 (Text-To-Text Transfer Transformer) model for producing human-like text.',
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/ContentCraftAI',
    packages=find_packages(),
    install_requires=[
        'torch',
        'transformers',
        'matplotlib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
