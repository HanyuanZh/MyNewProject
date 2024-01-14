My New Project
===============================

.. image:: https://github.com/HanyuanZh/MyNewProject/raw/master/project-icon.png
   :height: 128px
   :width: 128px
   :target: https://github.com/HanyuanZh/MyNewProject
   :alt: Logo

.. image:: https://github.com/HanyuanZh/MyNewProject/badges/master/build.svg
   :target: https://github.com/HanyuanZh/MyNewProject/pipelines
   :alt: GitLab-CI test status

.. image:: https://github.com/HanyuanZh/MyNewProject/badges/master/coverage.svg
    :target: https://github.com/HanyuanZh/MyNewProject/commits/master
    :alt: Test coverage

.. image:: https://readthedocs.org/projects/MyNewProject/badge/?version=latest
    :target: http://MyNewProject.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status



Author: hanyuan

My New Project is part of the `SciKit-Surgery`_ software project, developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_, part of `University College London (UCL)`_.

My New Project is tested on Python 3.8 but should support other modern Python versions.

My New Project is currently a demo project, which will add/multiply two numbers. Example usage:

::

    python mynewproject.py 5 8
    python mynewproject.py 3 6 --multiply

Please explore the project structure, and implement your own functionality.

Developing
----------

Cloning
^^^^^^^

You can clone the repository using the following command:

::

    git clone https://github.com/HanyuanZh/MyNewProject


Create virtual environment
^^^^^^^^^^^^^^^^^^^^^^^^^^

You can create a mamba virtual environment using

::

    mamba create -n My New ProjectVE python=3.8 pip -c conda-forge
    mamba activate My New ProjectVE
    pip install -r requirements-dev.txt

Running tests
^^^^^^^^^^^^^
Pytest is used for running unit tests:
::

    python -m pytest


Linting
^^^^^^^

This code conforms to the PEP8 standard. Pylint can be used to analyse the code:

::

    pylint --rcfile=tests/pylintrc mynewproject


Installing
----------

You can pip install directly from the repository as follows:

::

    pip install git+https://github.com/HanyuanZh/MyNewProject



Contributing
^^^^^^^^^^^^

Please see the `contributing guidelines`_.


Useful links
^^^^^^^^^^^^

* `Source code repository`_
* `Documentation`_


Licensing and copyright
-----------------------

Copyright 2023 University College London.
My New Project is released under the BSD-3 license. Please see the `license file`_ for details.


Acknowledgements
----------------

Supported by `Wellcome`_ and `EPSRC`_.


.. _`Wellcome EPSRC Centre for Interventional and Surgical Sciences`: http://www.ucl.ac.uk/weiss
.. _`source code repository`: https://github.com/HanyuanZh/MyNewProject
.. _`Documentation`: https://MyNewProject.readthedocs.io
.. _`SciKit-Surgery`: https://github.com/SciKit-Surgery
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: https://github.com/HanyuanZh/MyNewProject/blob/master/CONTRIBUTING.rst
.. _`license file`: https://github.com/HanyuanZh/MyNewProject/blob/master/LICENSE