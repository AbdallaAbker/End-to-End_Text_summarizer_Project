import setuptools

with open("README.md", "r", encoding="utf-8") as f:

    long_description = f.read()

__version__ = "0.0.0"


REPO_name = "End-to-End_Text_summarizer_Project"
AUTHOR_USER_NAME = "Abdalla Abker"
SRC_REPO = "text_summarizer"
AUTHOR_EMAIL = "aabdalla1088@gmail.com"


setuptools.setup(
                    name=REPO_name,
                    version=__version__,
                    authour=AUTHOR_USER_NAME,
                    author_email=AUTHOR_EMAIL,
                    description="End-to-End_Text_summarizer_Project Python Pachake",
                    long_description=long_description,
                    long_description_content_type="text/markdown",
                    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_name}",
                    project_urls={
                        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_name}/issues",   
                    },

                    package_dir={"": "src"},
                    packages=setuptools.find_packages(where="src")
                )