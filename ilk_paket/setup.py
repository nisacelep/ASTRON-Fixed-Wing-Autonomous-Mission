from setuptools import find_packages, setup

package_name = 'ilk_paket'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nisa',
    maintainer_email='nisa@todo.todo',
    description='PX4 sabit kanat kontrolu: ROS 2 ve uXRCE-DDS ile telemetri ve ucus komutlari',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'ilk_dinleyici = ilk_paket.ilk_dinleyici:main',
            'arm_gonderici = ilk_paket.arm_gonderici:main',
            'rtl_gonderici = ilk_paket.rtl_gonderici:main',
        ],
    },
)
