from distutils.core import setup

setup(
    name='vpn-killswitch',
    version='1.0',
    packages=[''],
    url='https://github.com/jandie/vpn-killswitch',
    license='GPL-3.0',
    author='Jandie Hendriks',
    author_email='jandie@protonmail.com',
    description='VPN killswitch for processes',
    requires=['duckduckgo', 'psutil']
)
