Differential Privacy Laplace Documentation
===========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Privacy budget
--------------

The privacy budget ``epsilon`` defines how much privacy protection to apply.

  - If ``epsilon`` is large, less noise will be added and therefore more information leakage exists, so less privacy protection will be present.
  - If ``epsilon`` is small (must be larger than zero), more noise will be added and therefore less information leakage exists, so more privacy protection will be present.

DiffPrivStatistics
-------------------

.. currentmodule:: diffpriv_laplace

.. autoclass:: DiffPrivStatistics
    :members:

DiffPrivLaplaceMechanism
-------------------------

.. currentmodule:: diffpriv_laplace

.. autoclass:: DiffPrivLaplaceMechanism
    :members:
    :special-members:

Indices and tables
==================

* :ref:`genindex`
