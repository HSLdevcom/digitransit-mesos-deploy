Ansible Azure roles for digitransit deployment
=========

Roles built to deploy a digitransit to microsoft azure platform 

It will deploy: 

*Azure application gateway for SSL offload and traffic managment
*Azure container service using DC/OS as the orchestrator
*Digitransit docker containers from dockerhub to run the service
*CDN service to host static content for digitransit project. 


some example playbooks are included and can be executed like so.

ansible-playbook -i hosts playbookname.yml 

Requirements
------------

AZURE xplat-cli needs to be installed and default subscription set. 
SSH tunel to DC/OS master


License
-------

BSD


Author Information
------------------

mark.bryan@cgi.com
