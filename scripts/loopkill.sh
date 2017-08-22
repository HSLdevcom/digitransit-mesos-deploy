# loops through nodes in a cluster and kills docker containers that are
# not started by mesos
dig +noall +answer slave.mesos 2> /dev/null | awk '{print $5}' | while read HOST ; do ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -n $HOST "sudo docker ps | grep -v mesos | grep -v CONTAINER | awk '{print \$1}' | while read i ; do sudo docker kill \$i ; done" ; done
