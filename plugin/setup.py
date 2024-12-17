from setuptools import setup, find_packages
setup(
    name="comment_translator",
    version="1.0",
    packages=find_packages(),
    install_requires=["googletrans==4.0.0-rc1"],
    entry_points={
        "console_scripts": [
            "translate-comments=comment_translator:translate_file_comments",
        ],
    },
)