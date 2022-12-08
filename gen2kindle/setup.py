from setuptools import setup


with open("README.md", "r") as fh:
		long_description = fh.read()
		
setup(name='gen2kindle',
			version='1.2',
			description='Search, download books,articles etc. from Libgen and send to your kindle.',
			url='http://github.com/shashanoid/GenToKindle',
			author='Shashanoid',
			author_email='shashanoid@gmail.com',
			license='MIT',
			long_description=long_description,
			long_description_content_type="text/markdown",
			packages=['gen2kindle'],
			scripts=['bin/gen2kindle', 'bin/get_libgen_data.py', 'bin/kindlegen', 'bin/kindle_mail.py'],
			install_requires=[
					'beautifulsoup4==4.6.3',
					'certifi==2022.12.7',
					'chardet==3.0.4',
					'html5lib==1.0.1',
					'idna==2.7',
					'tqdm==4.25.0',
					'requests==2.19.1',
					'six==1.11.0',
					'urllib3==1.23',
					'webencodings==0.5.1',
			],
			zip_safe=False)