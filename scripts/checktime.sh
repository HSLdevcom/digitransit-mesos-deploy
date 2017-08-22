# Loops nodes to see if their clock is broken
dig +noall +answer slave.mesos 2> /dev/null | awk '{print $5}' | while read HOST ; do echo $HOST && ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -n $HOST "timedatectl status" 2> /dev/null ; done
