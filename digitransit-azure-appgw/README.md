Role Name
=========

Ansible role to deploy an application gateway for AZURE, the gateway manages traffic for digitransit platform

Requirements
------------

You will need the azure xplat-cli installed and authenticated agaist you Azure subscriptions additional set the default subscription to the one in which u want to deploy

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

In order for gateway to fully work the digitransit-acs and acs-deploy roles need to be run. 

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      roles:
         - { role: digitransit-azure-appgw }

License
-------

BSD

Author Information
------------------

mark.bryan@cgi.com
