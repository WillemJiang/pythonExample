Usage
=====
This the Usage page to show how to install and use this application

Greeting
----------------

To send the greeting message
you can use the ``greet`` function:

.. autofunction:: example.main.greet

The ``name`` parameter should be either ``"Tom"``, ``"Jerry"``,
or ``"veggies"``. Otherwise, :py:func:`main.greet`
will raise an exception.

.. autoexception:: example.main.InvalidNameError

For example:

>>> import example.main
>>> example.main.greet("Tom")
Hello, Tom