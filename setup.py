from setuptools import find_packages, setup

# Installation
config = {
    'name': 'developer_test_solution',
    'version': '0.1.0',
    'description': 'Giskard Machine learning position researcher test.',
    'author': 'Abdoulaye Koroko',
    'author_email': 'abdoulayekoroko@gmail.com',
    'packages': find_packages(),
    'zip_safe': True
}

setup(**config)