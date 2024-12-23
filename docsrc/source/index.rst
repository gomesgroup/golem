Golem: An algorithm for robust experiment and process optimization
==================================================================

.. image:: https://github.com/aspuru-guzik-group/golem/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/aspuru-guzik-group/golem/actions/workflows/ci.yml
.. image:: https://codecov.io/gh/aspuru-guzik-group/golem/branch/master/graph/badge.svg?token=pHQ8Z50qf8
    :target: https://codecov.io/gh/aspuru-guzik-group/golem

**Golem** is a Python tool that allows to compute the expectation and variance of black-box objective functions
based on specified uncertainty/noise in the input variables. It can thus be used to see how different levels of input
uncertainty might affect the location of the optimum, or it can be used in conjunction with optimization algorithms
to enable robust optimization.

At the basis of the algorithm is the use of supervised tree-based models, such as regression trees and random forests.
Please refer to the `publication <https://arxiv.org/abs/2103.03716>`_ for the details of the approach.

.. toctree::
   :maxdepth: 1
   :caption: User documentation

   install
   golem_class
   distributions/index
   examples/index


Citation
--------
If you use **Golem** in scientific publications, please cite the following paper:

* M. Aldeghi, F. Häse, R.J. Hickman, I. Tamblyn, A. Aspuru-Guzik. `Golem: An algorithm for robust experiment and process optimization <https://arxiv.org/abs/2103.03716>`_. *arXiv* (2021), 2103.03716

::

    @misc{golem,
      title={Golem: An algorithm for robust experiment and process optimization},
      author={Matteo Aldeghi and Florian Häse and Riley J. Hickman and Isaac Tamblyn and Alán Aspuru-Guzik},
      year={2021},
      eprint={2103.03716},
      archivePrefix={arXiv},
      primaryClass={math.OC}
      }


License
-------
**Golem** is distributed under an MIT License.
