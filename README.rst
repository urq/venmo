.. image:: https://img.shields.io/pypi/v/venmo.svg
    :target: https://pypi.python.org/pypi/venmo

.. image:: https://travis-ci.org/zackhsi/venmo.svg?branch=master
    :target: https://travis-ci.org/zackhsi/venmo

Venmo
=====

Pay or charge people on the command line!

::

    $ venmo pay @zackhsi 23.19 "Thanks for the beer <3"
    $ venmo charge 19495551234 23.19 "That beer wasn't free!"

Installation
------------

``venmo`` can be installed via ``pip``.

::

    $ pip install venmo

Setup
-----
Set up venmo by running:

::

    $ venmo configure

    > Venmo email [None]: zackhsi@gmail.com
    > Venmo password [None]:
    > Bank Account ID (Optional, see https://github.com/zackhsi/venmo/blob/master/README.rst for instructions) [None]:
    > Verification code: 908126  # for 2 factor authentication

That's it!

Finding your Bank Account ID
----------------------------
You can set the optional configuration parameter `Bank Account ID` to enable
transfering money from your venmo balance to your bank. The `Bank Account ID`
is a UUID that is Venmo's unique reference to your account. To find it, do the
following:

1. Navigate to venmo.com in your browser and sign in.
2. Click on the "Transfer to Bank" link to bring up the Transfer modal.
3. You will see your bank accounts listed in the modal. Right-click on the
   bank of interest and inspect the HTML element.
4. Traverse the parents of the selected DOM node (navigate up the DOM tree)
   to the first tag. It should have a "ba-id" property whose value is a UUID.
   This is your bank ID.

Contributing
------------
Pull requests welcome! To get started, first clone the repository:

::

    $ git clone git@github.com:zackhsi/venmo.git

Create a virtualenv containing an editable installation of venmo, plus
development dependencies:

::

    $ make init

Activate the virtualenv:

::

    $ pipenv shell

Run tests:

::

    $ make test
