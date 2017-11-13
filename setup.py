from setuptools import setup

setup(
    name='reche',
    version='0.1',
    py_modules=['app'],
    url='https://github.com/aninternetof/reche',
    license='MIT',
    author='Brady Hurlburt',
    author_email='bradyhurburt@gmail.com',
    description='Set your MacOS desktop to a Tumblr feed',
    install_requires=[
        'beautifulsoup4',
        'click',
        'requests',
        'pillow'
    ],
    entry_points='''
    [console_scripts]
    reche=app:cli
    ''',
)
