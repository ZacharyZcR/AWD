# coding=utf-8

from setuptools import setup, find_packages

setup(
	name='awdphpspear',
	version='0.0.7',
	description=(
		'A tools for AWD attack.'
	),
	author='ZacharyZcR',
	author_email='2903735704@qq.com',
	maintainer='Mystery Security',
	maintainer_email='zacharyzcr@hi-ourlife.com',
	license='MIT License',
	packages=find_packages(),
	platforms=["all"],
	url='https://github.com/ZacharyZcR/AWD',
	install_requires=[
		'requests',
	],
	classifiers=[
		'Development Status :: 4 - Beta',
		'Operating System :: OS Independent',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Programming Language :: Python',
		'Programming Language :: Python :: Implementation',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Topic :: Software Development :: Libraries'
	],
)