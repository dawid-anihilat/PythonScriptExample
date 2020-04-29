pgbackup
========

CLI for backuping remote POSTGRESSQL database locally or to aws s3

Preparing for development
-----------------------

1. Ensure ``pip`` and ``pipenv`` are installed
2. Clone reposiroty ....
3. Fetch development dependencies: `make install`

Usage
-----

Pass in a full database URl, storage driver and destionation

S3 Example

::

  $ pgbackup postgres://bob@example.com:5432 --driver s3 backups

Local Example
-------------

::

  $  pgbackup postgres://bob@example.com:5432 --driver local /var/local/db/

Running Tests
-------------

Run test locallly using ``make`` if virtualenv is active

::

 $ make

If virtualenv isn't active then use:

::

  $ pipenv run make

