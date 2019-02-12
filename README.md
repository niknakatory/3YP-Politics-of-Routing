# 3YP-Politics-of-Routing

## Datasets

The `data/` repository directory contains datasets on various types of attacks types, extracted by the sources listed in the [wiki page](https://github.com/niknakatory/3YP-Politics-of-Routing/wiki#data-on-detected-routing-attacks):

* `badpackets_mirai.txt`
   Contains the IP interfaces and some relevant metadata of infected hosts that are part of botnets that resemble the Mirai botnet. 
   These IPs have been extracted by the BadPackets website using the `code/badpackets_mirai.py` script.

* `botnet_ips_2017-2019.zip`
   Contains all the IP interfaces observed as part of Mirai-like botnets between 2017-2019. The format is:
   <ip_address> <date_first_seen> <date_last_seen> <difference between first seen and last seen in_seconds>
   
* `hijacks_2018.csv`
   Contains the detected BGP Prefix Hijackings detected by BGPMon.

* `asn_countries_names.txt`
   The mapping between AS Numbers (ASNs), AS Names, and countries ([2-letter ISO codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2))
The format of the files is explained in the comment section at the top of each file.
The lines in the comment section start with `#`.

* `country_dependencies.txt`
   The fraction of paths that traverse another country. 
   For each country, the file has line with the following format: `CC|CC,fraction<tab>CC,fraction<tab>...`, where CC is the country code. For example, consider the line:
   
   `DE|CN,0.00695828101271	DE,0.169236143727	GB,0.0338861193408	US,0.379655359392	VE,4.59660898305e-06	VG,2.21622218826e-06	VN,0.00303515732797	ZA,0.00212667039539	IS,4.00561639952e-05`
   
   The above line starts with "`DE|`", which means that it's about German ASes. Then there is the list of countries and corresponding fractions of paths that go through these countries. `US,0.379655359392` means that 37% of the paths go through US-based ASes, while `CN,0.00695828101271` means that 0.6% of the paths go through Chinese ASes. 

* `internet_penetration.csv`
  Stats on Internet penetration per country. The format is:  
  `country name,country code,IP addresses (million),IP addresses per capita,Fraction of total IP addresses`
   
## Wiki Pages

* [Relevant literature on malicious routing behaviour](https://github.com/niknakatory/3YP-Politics-of-Routing/wiki)
* [Data on Detected Attacks](https://github.com/niknakatory/3YP-Politics-of-Routing/wiki#data-on-detected-routing-attacks)
* [Utilities for data analysis](https://github.com/niknakatory/3YP-Politics-of-Routing/wiki#utilities)


## Propensity to conduct malicious routing:

* Do they operate publically disclosed mass surveillance programs?
* Has their surveillance been unlawful now or in the past? (boomeranging)
* Frequency host nation appears in DDoSDB/badpackets/hijacks2018 as instigator. 
* 

## Exposure of Citizens to malicious routing:

* Are there any protection measures? (Schengen Zone)
* Effectiveness of protection...
* Geolocation in relation to other hegemonic nations that perform malicious routing. 
* Amount of independent paths (robustness)
* Level of surveillance of nation's own citizens. 
* Are citizens exposed to online social engineering policies from their own government?
