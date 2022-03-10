from setuptools import setup

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup (
    name="connection_drive",
    version="0.0.1",
    author="ivan_araujo",
    author_email="ivanribeiro_araujo@hotmail.com",
    description="conexão mysql, postgres e cassandra para ingestão de dados",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link"    
    )

