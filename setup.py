# Copyright 2023-present, the unsloth authors.
# Licensed under the Apache License, Version 2.0

from setuptools import setup, find_packages
import re
import os


def get_version():
    """Read version from __init__.py or return default."""
    version_file = os.path.join(os.path.dirname(__file__), "unsloth", "__init__.py")
    if os.path.exists(version_file):
        with open(version_file, "r", encoding="utf-8") as f:
            content = f.read()
        match = re.search(r'^__version__\s*=\s*["\']([^"\']+)["\']', content, re.MULTILINE)
        if match:
            return match.group(1)
    return "2024.1.0"


def get_long_description():
    """Read long description from README if available."""
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return "Unsloth - Fast LLM fine-tuning with minimal memory usage."


setup(
    name="unsloth",
    version=get_version(),
    author="unsloth authors",
    author_email="unsloth@unsloth.ai",
    description="2-5x faster, 80% less memory LLM fine-tuning",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/unslothai/unsloth",
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*"]),
    python_requires=">=3.9",
    install_requires=[
        "torch>=2.1.0",
        "transformers>=4.38.0",
        "datasets>=2.16.0",
        "sentencepiece>=0.1.99",
        "tqdm",
        "psutil",
        "wheel>=0.42.0",
        "packaging>=23.1",
        "numpy",
        "peft>=0.7.0",
        "accelerate>=0.26.0",
        "bitsandbytes>=0.42.0",
        # Relaxed protobuf constraint - protobuf 4.x works fine in my testing
        "protobuf>=3.20.0",
        "huggingface_hub",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov",
            "black",
            "isort",
            "flake8",
            "mypy",
        ],
        "colab": [
            "triton>=2.1.0",
            "xformers",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "llm",
        "fine-tuning",
        "lora",
        "qlora",
        "transformers",
        "efficient training",
        "memory optimization",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/unslothai/unsloth/issues",
        "Documentation": "https://github.com/unslothai/unsloth/wiki",
        "Source Code": "https://github.com/unslothai/unsloth",
    },
)
