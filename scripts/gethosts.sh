# prints hostnames of servers
dig +noall +answer slave.mesos 2> /dev/null | awk '{print $5}' | while read HOST ; do ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -n $HOST "hostname" 2> /dev/null; done

