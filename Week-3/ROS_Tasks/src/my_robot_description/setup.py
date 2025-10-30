from setuptools import setup

package_name = 'my_robot_description'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='YourName',
    maintainer_email='youremail@example.com',
    description='My custom robot description package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'diff_drive = my_robot_description.diff_drive:main',
        ],
    },
)
