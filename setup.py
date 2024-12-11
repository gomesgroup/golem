"""Golem: An Algorithm for Robust Experiment and Process Optimization
"""

import versioneer
from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize
import numpy as np
import sysconfig


# readme file
def readme():
    with open('README.md') as f:
        return f.read()


# extensions
extensions = [
    Extension(
        "golem.extensions",
        ["src/golem/extensions.pyx"],
        include_dirs=[np.get_include()],
        define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
    )
]

# -----
# Setup
# -----
setup(name='matter-golem',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Golem: An Algorithm for Robust Experiment and Process Optimization',
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
      ],
      url='https://github.com/aspuru-guzik-group/golem',
      author='Matteo Aldeghi',
      author_email='matteo.aldeghi@vectorinstitute.ai',
      license='MIT',
      packages=find_packages(where='src'),
      package_dir={'': 'src'},
      zip_safe=False,
      tests_require=['pytest', 'deap'],
      install_requires=['numpy', 'scipy>=1.4', 'scikit-learn', 'pandas'],
      python_requires=">=3.7",
      ext_modules=cythonize(extensions)
      )
