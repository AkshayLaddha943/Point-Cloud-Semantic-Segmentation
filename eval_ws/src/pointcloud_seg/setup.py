from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'pointcloud_seg'

def recursive_data_files(src_directory, dest_directory):
    paths = []
    for (path, directories, filenames) in os.walk(src_directory):
        rel_path = os.path.relpath(path, src_directory)
        dest_path = os.path.join(dest_directory, rel_path)
        files = [os.path.join(path, filename) for filename in filenames]
        paths.append((dest_path, files))
    return paths

data_files = recursive_data_files('models', os.path.join('share', package_name, 'models'))

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='akshladdhs',
    maintainer_email='akshaymahesh10@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'pointcloud_segmentation = pointcloud_seg.point_cloud_segmentation:main',
        ],
    },
)
