# Research
PDC and PMU simulation using SDN

# Network Simulation tool
Mininet
use command : sudo mn --topo single,6 --mac --controller remote

#Open flow controller
Pox
use command : ~pox./pox.py controller
We are modifying default forward.l2_learning code to suit are simulation

#Setup
6 host h1 to h6 and one switch s1.

Host 1 and host 2 will act as PDC (Server)
Host 3 and host 4 will act as PMU (Client)

H5 is the end application which processes the data.
