from setuptools import setup

setup(name='genkindle',
      version='1.0',
      description='Search, download from Libgen and send to your kindle.',
      url='http://github.com/shashanoid/GenToKindle',
      author='Shashanoid',
      author_email='shashanoid@gmail.com',
      license='MIT',
      packages=['gentokindle'],
      scripts=['bin/gentokindle', 'bin/get_libgen_data.py', 'bin/kindlegen', 'bin/kindle_mail.py'],
      install_requires=[
          'beautifulsoup4==4.6.3',
          'certifi==2018.8.24',
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