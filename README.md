# 3YP-Politics-of-Routing

## Datasets

The 'data/' repository directory contains datasets on various types of attacks types, extracted by the sources listed in the [wiki page](https://github.com/niknakatory/3YP-Politics-of-Routing/wiki#data-on-detected-routing-attacks):

* `badpackets_mirai.txt`
   Contains the IP interfaces and some relevant metadata of infected hosts that are part of botnets that resemble the Mirai botnet. 
   These IPs have been extracted by the BadPackets website using the `code/badpackets_mirai.py` script.
* `hijacks_2018.csv`
   Contains the detected BGP Prefix Hijackings detected by BGPMon.
   
The format of the files is explained in the comment section at the top of each file.
The lines in the comment section start with `#`.

## Wiki Pages

* [Relevant literature on malicious routing behaviour](https://github.com/niknakatory/3YP-Politics-of-Routing/wiki)
* [Data on Detected Attacks](https://github.com/niknakatory/3YP-Politics-of-Routing/wiki#data-on-detected-routing-attacks)
* [Utilities for data analysis](https://github.com/niknakatory/3YP-Politics-of-Routing/wiki#utilities)
