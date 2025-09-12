:py:mod:`BlackWidowPipeline.calculate_extinction_correction`
============================================================

.. py:module:: BlackWidowPipeline.calculate_extinction_correction

.. autodoc2-docstring:: BlackWidowPipeline.calculate_extinction_correction
   :allowtitles:

Module Contents
---------------

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`calculate_ebv_from_halpha_hbeta_ratio <BlackWidowPipeline.calculate_extinction_correction.calculate_ebv_from_halpha_hbeta_ratio>`
     - .. autodoc2-docstring:: BlackWidowPipeline.calculate_extinction_correction.calculate_ebv_from_halpha_hbeta_ratio
          :summary:
   * - :py:obj:`calculate_Alambda_from_ebv <BlackWidowPipeline.calculate_extinction_correction.calculate_Alambda_from_ebv>`
     - .. autodoc2-docstring:: BlackWidowPipeline.calculate_extinction_correction.calculate_Alambda_from_ebv
          :summary:
   * - :py:obj:`calc_extinction_correction <BlackWidowPipeline.calculate_extinction_correction.calc_extinction_correction>`
     - .. autodoc2-docstring:: BlackWidowPipeline.calculate_extinction_correction.calc_extinction_correction
          :summary:
   * - :py:obj:`apply_extinction_correction <BlackWidowPipeline.calculate_extinction_correction.apply_extinction_correction>`
     - .. autodoc2-docstring:: BlackWidowPipeline.calculate_extinction_correction.apply_extinction_correction
          :summary:
   * - :py:obj:`unapply_extinction_correction <BlackWidowPipeline.calculate_extinction_correction.unapply_extinction_correction>`
     - .. autodoc2-docstring:: BlackWidowPipeline.calculate_extinction_correction.unapply_extinction_correction
          :summary:

API
~~~

.. py:function:: calculate_ebv_from_halpha_hbeta_ratio(Halpha_map: numpy.ndarray, Hbeta_map: numpy.ndarray) -> numpy.ndarray
   :canonical: BlackWidowPipeline.calculate_extinction_correction.calculate_ebv_from_halpha_hbeta_ratio

   .. autodoc2-docstring:: BlackWidowPipeline.calculate_extinction_correction.calculate_ebv_from_halpha_hbeta_ratio

.. py:function:: calculate_Alambda_from_ebv(ebv_map: numpy.ndarray, wavelength: float) -> numpy.ndarray
   :canonical: BlackWidowPipeline.calculate_extinction_correction.calculate_Alambda_from_ebv

   .. autodoc2-docstring:: BlackWidowPipeline.calculate_extinction_correction.calculate_Alambda_from_ebv

.. py:function:: calc_extinction_correction(Halpha_map: numpy.ndarray, Hbeta_map: numpy.ndarray, wavelength: float) -> numpy.ndarray
   :canonical: BlackWidowPipeline.calculate_extinction_correction.calc_extinction_correction

   .. autodoc2-docstring:: BlackWidowPipeline.calculate_extinction_correction.calc_extinction_correction

.. py:function:: apply_extinction_correction(flux_map: numpy.ndarray, Alambda_map: numpy.ndarray) -> numpy.ndarray
   :canonical: BlackWidowPipeline.calculate_extinction_correction.apply_extinction_correction

   .. autodoc2-docstring:: BlackWidowPipeline.calculate_extinction_correction.apply_extinction_correction

.. py:function:: unapply_extinction_correction(corrected_flux_map: numpy.ndarray, Alambda_map: numpy.ndarray) -> numpy.ndarray
   :canonical: BlackWidowPipeline.calculate_extinction_correction.unapply_extinction_correction

   .. autodoc2-docstring:: BlackWidowPipeline.calculate_extinction_correction.unapply_extinction_correction
