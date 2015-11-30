ufw_add_host
============

Very simple script to add all the known ip addresses from a particular host
as exception to ufw.

I use this myself for adding the ips from my VPN as exception, since I don't want DNS leaks but want
to be able to connect to the VPN servers nevertheless.

Usage
-----

`ufw_add_host.py example.com`

This will add all the ip addresses from example.com to ufw as exception.
