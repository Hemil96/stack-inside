from setuptools import setup

setup(
    name='Tech Inside',
    version='0.1',
    py_modules=['sicli'],
    install_requires=[
        'Click',
        'BeautifulSoup',
        'bs4',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        techinside=sicli:cli
    ''',
)
