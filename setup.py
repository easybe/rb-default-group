from setuptools import setup


PACKAGE = "default_group"
VERSION = "0.1"

setup(
    name=PACKAGE,
    version=VERSION,
    description="""An extension that adds all new users to a group.
 This is good for giving all users certain permissions.""",
    author="Ezra Buehler",
    packages=["default_group"],
    entry_points={
        'reviewboard.extensions':
            '%s = default_group.extension:DefaultGroup' % PACKAGE,
    },
    package_data={
        'default_group': [
            'htdocs/css/*.css',
            'htdocs/js/*.js',
            'templates/default_group/*.txt',
            'templates/default_group/*.html',
        ],
    }
)
