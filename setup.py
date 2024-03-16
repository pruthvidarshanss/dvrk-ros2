from setuptools import setup
from glob import glob
import os

package_name = 'urdf_dvrk'

setup(
    name=package_name,
    version='0.0.2',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join("share", package_name, "launch/"), glob("launch/*.launch.*")),
        (os.path.join("share", package_name, "xacro/"), glob("xacro/*.xacro")),
        (os.path.join("share", package_name, "xacro/"), glob("xacro/*.yaml")),
        (os.path.join("share", package_name, "xacro/meshes/"), glob("xacro/meshes/*.stl")),
        (os.path.join("share", package_name, "xacro/meshes/hand/"), glob("xacro/meshes/hand/*.stl")),
        (os.path.join("share", package_name, "xacro/meshes/hand/taxels/"), glob("xacro/meshes/hand/taxels/*.stl")),
        (os.path.join("share", package_name, "xacro/meshes/hand/taxels/L1/"), glob("xacro/meshes/hand/taxels/L1/*.stl")),
        (os.path.join("share", package_name, "xacro/meshes/hand/taxels/L2/"), glob("xacro/meshes/hand/taxels/L2/*.stl")),
        (os.path.join("share", package_name, "xacro/meshes/hand/taxels/L3/"), glob("xacro/meshes/hand/taxels/L3/*.stl")),
        (os.path.join("share", package_name, "xacro/meshes/ecm/"), glob("xacro/meshes/ecm/*.STL")),
        (os.path.join("share", package_name, "xacro/meshes/psm/"), glob("xacro/meshes/psm/*.STL")),
        (os.path.join("share", package_name, "xacro/meshes/suj/"), glob("xacro/meshes/suj/*.STL")),
        (os.path.join("share", package_name, "rviz/"), glob("rviz/*.rviz")),
        (os.path.join("share", package_name, "worlds/"), glob("worlds/*.world")),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Pruthvi',
    maintainer_email='darshupruthvi007@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
