Digitransit Azure CDN 
=========

The role creates a cdn endpoint which points to the api to cache static content

Requirements
------------

Azure xplat-cli install with valid azure subscription


Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

Azure

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: localhost
      roles:
         - { role: digitransit-azure-cdn }

License
-------

BSD

Author Information
------------------

mark.bryan@cgi.com
