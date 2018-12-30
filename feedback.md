### Motivation for research

Section 1.2 is nice but I would just suggest a slightly different angle in framing the motivation. 

The question is whether we can find evidence of malicious routing practices that are politically-motivated. 
Countries that restrict freedoms (both individual and freedom of press) have mechanisms in place to monitor Internet 
activity of users and organizations. Such countries would be expected to have lower levels of malicious activity. 
Observing the contrary, i.e. malicious routing from countries that tightly control their Internet would suggest state-motivated 
cyber-attacks. Consider the following as a very crude example of a potential opening paragraph:

> Over the past years we have observed an increase in the frequency and severity of cyber threats, including DDoS attacks, malware, and cyber-espionage [1, 2]. Many governments argue that tighter control of on-line activities - at the expense of privacy and freedom of expression - can be an effective tool against cyber-attacks [3]. Indeed, the Snowden leaks illustrated that such policies are indeed materialized and surveillance mechanisms are deployed more widely than previously thought. 
On the other hand, there are little evidence that such policies actually limit the cyber risks. Anecdotal evidence suggest that state-sponsored cyber warfare is resonsible for the most catastrophic attacks [4,5]. This would imply that stricter control of the Internet by state actors may actually maximize attack vectors, many of which rely on malicious routing practices. To illuminate this debate, this project will explore how online freedom correlates with malicious routing.
>
>REFERENCES
>
> [1] https://otalliance.org/system/files/files/initiative/documents/ota_cyber_incident_trends_report_jan2018.pdf  
> [2] https://www.jbs.cam.ac.uk/fileadmin/user_upload/research/centres/risk/downloads/crs-cyber-risk-outlook-2018.pdf  
> [3] https://www.brookings.edu/articles/cybercrime-dilemma-is-it-possible-to-guarantee-both-security-and-privacy/  


## Mirai-like attacks by origin country

The following plot is extremely interesting. It would be interesting to plot the number of attacks per country as proportion to the country's share of IPv4 address space and ASNs.

![Mirai-like attacks by country](https://github.com/niknakatory/3YP-Politics-of-Routing/blob/master/figures/mirai-like-attacks-by-origin-counry.png?raw=true)

The page below lists the ASNs and number of IPv4 addresses per country:
- https://bgp.he.net/report/world 
- https://bgp.he.net/report/prefixes#_countriesv4
