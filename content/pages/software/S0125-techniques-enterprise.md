Title: enterprise Techniques
Template: general/json
save_as: software/S0125/S0125-enterprise-layer.json
json: {"description": "Enterprise techniques used by Remsec, ATT&CK software S0125 v1.0", "name": "Remsec (S0125)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1087", "comment": "Remsec can obtain a list of users.[2]"}, {"score": 1, "techniqueID": "T1003", "comment": "Remsec can dump the SAM database.[2]"}, {"score": 1, "techniqueID": "T1094", "comment": "Remsec is capable of using ICMP, TCP, and UDP for C2.[3][4]"}, {"score": 1, "techniqueID": "T1025", "comment": "Remsec has a package that collects documents from any inserted USB sticks.[2]"}, {"score": 1, "techniqueID": "T1089", "comment": "Remsec can add or remove applications or ports on the Windows firewall or disable it entirely.[2]"}, {"score": 1, "techniqueID": "T1048", "comment": "Remsec can exfiltrate data via a DNS tunnel or email, separately from its C2 channel.[4]"}, {"score": 1, "techniqueID": "T1052", "comment": "Remsec contains a module to move data from airgapped networks to Internet-connected systems by using a removable USB device.[4]"}, {"score": 1, "techniqueID": "T1068", "comment": "Remsec has a plugin to drop and execute vulnerable Outpost Sandbox or avast! Virtualization drivers in order to gain kernel mode privileges.[2]"}, {"score": 1, "techniqueID": "T1083", "comment": "Remsec is capable of listing contents of folders on the victim. Remsec also searches for custom network encryption software on victims.[3][4][2]"}, {"score": 1, "techniqueID": "T1107", "comment": "Remsec is capable of deleting files on the victim. It also securely removes itself after collecting and exfiltrating data.[3][4][2]"}, {"score": 1, "techniqueID": "T1056", "comment": "Remsec contains a keylogger component.[3][2]"}, {"score": 1, "techniqueID": "T1036", "comment": "The Remsec loader implements itself with the name Security Support Provider, a legitimate Windows function. Various Remsec .exe files mimic legitimate file names used by Microsoft, Symantec, Kaspersky, Hewlett-Packard, and VMWare. Remsec also disguised malicious modules using similar filenames as custom network encryption software on victims.[3][4]"}, {"score": 1, "techniqueID": "T1046", "comment": "Remsec has a plugin that can perform ARP scanning as well as port scanning.[2]"}, {"score": 1, "techniqueID": "T1027", "comment": "Some data in Remsec is encrypted using RC5 in CBC mode, AES-CBC with a hardcoded key, RC4, or Salsa20. Some data is also base64-encoded.[3][2]"}, {"score": 1, "techniqueID": "T1174", "comment": "Remsec harvests plain-text credentials as a password filter registered on domain controllers.[4]"}, {"score": 1, "techniqueID": "T1057", "comment": "Remsec can obtain a process list from the victim.[2]"}, {"score": 1, "techniqueID": "T1055", "comment": "Remsec can perform DLL injection.[2]"}, {"score": 1, "techniqueID": "T1105", "comment": "Remsec contains a network loader to receive executable modules from remote attackers and run them on the local victim. It can also upload and download files over HTTP and HTTPS.[3][2]"}, {"score": 1, "techniqueID": "T1018", "comment": "Remsec can ping or traceroute a remote host.[2]"}, {"score": 1, "techniqueID": "T1053", "comment": "Remsec schedules the execution one of its modules by creating a new scheduler task.[2]"}, {"score": 1, "techniqueID": "T1063", "comment": "Remsec has a plugin to detect active drivers of some security products.[2]"}, {"score": 1, "techniqueID": "T1071", "comment": "Remsec is capable of using HTTP, HTTPS, SMTP, and DNS for C2.[3][4][2]"}, {"score": 1, "techniqueID": "T1032", "comment": "Remsec's network loader encrypts C2 traffic with RSA and RC6.[3]"}, {"score": 1, "techniqueID": "T1095", "comment": "Remsec is capable of using ICMP, TCP, and UDP for C2.[3][4]"}, {"score": 1, "techniqueID": "T1082", "comment": "Remsec can obtain the OS version information, computer name, processor architecture, machine role, and OS edition.[2]"}, {"score": 1, "techniqueID": "T1016", "comment": "Remsec can obtain information about network configuration, including the routing table, ARP cache, and DNS cache.[2]"}, {"score": 1, "techniqueID": "T1049", "comment": "Remsec can obtain a list of active connections and open ports.[2]"}, {"score": 1, "techniqueID": "T1033", "comment": "Remsec can obtain information about the current user.[2]"}, {"score": 1, "techniqueID": "T1065", "comment": "A Remsec module has a default C2 port of 13000.[2]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Remsec", "color": "#66b1ff"}]}