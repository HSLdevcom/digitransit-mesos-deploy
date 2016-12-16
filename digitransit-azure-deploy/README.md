Role Name
=========

This role does this initial deployment of all containers that are needed to run the digitratnsit project onto ACS (Azure Container Service) the orchestrator used is DC/OS. 
the playbook deploys via the marathon API

Requirements
------------

ssh tunnel to DC/OS cluster is required for this playbook to run i.e 

sudo ssh -i $HOME/.ssh/yourkey_rsa -L 80:localhost:80 -f -N username@projectnamemgmt.azureregion.cloudapp.azure.com -p 2200


Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

requires digitransit-azure-acs


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: localhost
      roles:
         - { role: digitransit-azure-deploy }

License
-------

BSD

Author Information
------------------

mark.bryan@cgi.com
