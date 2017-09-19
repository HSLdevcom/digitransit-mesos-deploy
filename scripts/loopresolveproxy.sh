# Loops nodes to see if they can resolve digitransit-proxy ip
dig +noall +answer slave.mesos 2> /dev/null | awk '{print $5}' | while read HOST ; do echo $HOST && ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -n $HOST "host digitransit-proxy.marathon.l4lb.thisdcos.directory 2> /dev/null | tail -n 1 | grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b'" 2> /dev/null ; done

