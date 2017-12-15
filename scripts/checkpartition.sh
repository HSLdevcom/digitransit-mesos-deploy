# Loops nodes to see if a docker partition is missing
dig +noall +answer slave.mesos 2> /dev/null | awk '{print $5}' | while read HOST ; do echo $HOST && ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -n $HOST "df -h" 2> /dev/null | grep "/dev/sdb2"; done
