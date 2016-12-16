Role Name
=========

Digitransit ACS role deploys an empty azure container service for deploy digitransit docker containers 

Requirements
------------

AZURE CLI 2.0 Preview in needed to setup the ACS cluster make sure you have python and python pip installed 

pip install azure-cli 


Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

Not dependant on any other role

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: localhost
      roles:
         - { role: digitranist-azure-acs }

License
-------

BSD

Author Information
------------------

mark.bryan@cgi.com
