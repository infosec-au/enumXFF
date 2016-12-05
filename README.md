All you need to do is run the tool from the terminal giving the following input:

- Page to attempt (`http/https://website.com/page`)
- The content length of the response that you get when you are denied
- The IP range you wish the tool to attempt through `X-Forwarded-For`

The tool will then simply request the given page with a range of IP addresses and then determine whether or not access to the said page is still forbidden.

`python enumXFF.py -t http://sketchysite.com/admin -badcl 234 -r 192.168.0.0-192.168.255.255`

The above command will attempt to request `http://sketchysite.com/admin` with all IP addresses in the range `192.168.0.0-192.168.255.255`. The python script takes advantage of asynchronous HTTP requests via the `requests-futures` module and hence should be fairly quick. Note, this tool only functions on Python2.

In addition to this, the enumXFF project on Github also contains a script called `generateIPs.py`. This will simply generate a list of comma delimited IP addresses that can be input directly to Burp's Intruder. If the tool isn't the best way for you, Burp's Intruder is a reliable option to fall back on.

To generate the IPs for the range 192.168.0.0-192.168.255.255, you would need to use the following command:

`python3 generateIPs.py -r 192.168.0.0-192.168.255.255 -o burp_xff_ips.txt`

Refer to this blog post for further details: https://shubh.am/enumerating-ips-in-x-forwarded-headers-to-bypass-403-restrictions/
