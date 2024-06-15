from setuptools import setup, find_packages

setup(
    name='Webcrawler',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'attrs==23.2.0',
        'beautifulsoup4==4.12.3',
        'certifi==2024.2.2',
        'cffi==1.16.0',
        'charset-normalizer==3.3.2',
        'chromedriver-binary-auto==0.3.1',
        'cryptography==42.0.7',
        'docutils==0.21.2',
        'fake-useragent==1.5.1',
        'h11==0.14.0',
        'idna==3.7',
        'importlib_metadata==7.1.0',
        'jaraco.classes==3.4.0',
        'jaraco.context==5.3.0',
        'jaraco.functools==4.0.1',
        'jeepney==0.8.0',
        'keyring==25.2.1',
        'lxml==5.2.1',
        'markdown-it-py==3.0.0',
        'mdurl==0.1.2',
        'more-itertools==10.2.0',
        'nh3==0.2.17',
        'outcome==1.3.0.post0',
        'packaging==24.0',
        'pkginfo==1.10.0',
        'pycparser==2.22',
        'Pygments==2.18.0',
        'PySocks==1.7.1',
        'python-dotenv==1.0.1',
        'readme_renderer==43.0',
        'requests==2.31.0',
        'requests-toolbelt==1.0.0',
        'rfc3986==2.0.0',
        'rich==13.7.1',
        'SecretStorage==3.3.3',
        'selenium==4.20.0',
        'setuptools==69.5.1',
        'sniffio==1.3.1',
        'sortedcontainers==2.4.0',
        'soupsieve==2.5',
        'trio==0.25.0',
        'trio-websocket==0.11.1',
        'typing-extensions==4.11.0',
        'urllib3==2.2.1',
        # Remove self-referencing dependency
        #'webcrawler @ file:///mnt/d/WebScrapper-Bot', 
        'webdriver-manager==4.0.1',
        'wheel==0.43.0',
        'wsproto==1.2.0',
        'zipp==3.18.2',
    ],
)