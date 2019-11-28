Title: enterprise Techniques
Template: general/json
save_as: groups/G0059/G0059-enterprise-layer.json
json: {"description": "Enterprise techniques used by Magic Hound, ATT&CK group G0059 v1.1", "name": "Magic Hound (G0059)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1098", "comment": "Magic Hound granted compromised email accounts read access to the email boxes of additional targeted accounts. The group then was able to authenticate to the intended victim's OWA (Outlook Web Access) portal and read hundreds of email communications for information on Middle East organizations.[2]"}, {"score": 1, "techniqueID": "T1059", "comment": "Magic Hound has used the command-line interface.[1]"}, {"score": 1, "techniqueID": "T1043", "comment": "Magic Hound malware has communicated with C2 servers over port 6667 (for IRC) and port 8080.[1]"}, {"score": 1, "techniqueID": "T1003", "comment": "Magic Hound stole domain credentials from Microsoft Active Directory Domain Controller and leveraged Mimikatz.[2]"}, {"score": 1, "techniqueID": "T1002", "comment": "Magic Hound has used RAR to stage and compress local folders.[2]"}, {"score": 1, "techniqueID": "T1114", "comment": "Magic Hound has collected .PST archives.[2]"}, {"score": 1, "techniqueID": "T1083", "comment": "Magic Hound malware can list a victim's logical drives and the type, as well the total/free space of the fixed devices. Other malware can list a directory's contents.[1]"}, {"score": 1, "techniqueID": "T1107", "comment": "Magic Hound has deleted and overwrote files to cover tracks.[1][2]"}, {"score": 1, "techniqueID": "T1143", "comment": "Magic Hound malware has a function to determine whether the C2 server wishes to execute the newly dropped file in a hidden window.[1]"}, {"score": 1, "techniqueID": "T1056", "comment": "Magic Hound malware is capable of keylogging.[1]"}, {"score": 1, "techniqueID": "T1027", "comment": "Magic Hound malware has used base64-encoded commands and files, and has also encrypted embedded strings with AES.[1]"}, {"score": 1, "techniqueID": "T1086", "comment": "Magic Hound has used PowerShell for execution and privilege escalation.[1][2]"}, {"score": 1, "techniqueID": "T1057", "comment": "Magic Hound malware can list running processes.[1]"}, {"score": 1, "techniqueID": "T1060", "comment": "Magic Hound malware has used Registry Run keys to establish persistence.[1]"}, {"score": 1, "techniqueID": "T1105", "comment": "Magic Hound has downloaded additional code and files from servers onto victims.[1]"}, {"score": 1, "techniqueID": "T1113", "comment": "Magic Hound malware can take a screenshot and upload the file to its C2 server.[1]"}, {"score": 1, "techniqueID": "T1064", "comment": "Magic Hound malware has used .vbs scripts for execution.[1]"}, {"score": 1, "techniqueID": "T1193", "comment": "Magic Hound sent malicious attachments to victims over email, including an Excel spreadsheet containing macros to download Pupy.[3]"}, {"score": 1, "techniqueID": "T1192", "comment": "Magic Hound sent shortened URL links over email to victims. The URLs linked to Word documents with malicious macros that execute PowerShells scripts to download Pupy.[3]"}, {"score": 1, "techniqueID": "T1194", "comment": "Magic Hound used various social media channels to spearphish victims.[3]"}, {"score": 1, "techniqueID": "T1071", "comment": "Magic Hound malware has used HTTP and IRC for C2.[1]"}, {"score": 1, "techniqueID": "T1082", "comment": "Magic Hound malware has used a PowerShell command to check the victim system architecture to determine if it is an x64 machine. Other malware has obtained the OS version, UUID, and computer/host name to send to the C2 server.[1]"}, {"score": 1, "techniqueID": "T1016", "comment": "Magic Hound malware gathers the victim's local IP address, MAC address, and external IP address.[1]"}, {"score": 1, "techniqueID": "T1033", "comment": "Magic Hound malware has obtained the victim username and sent it to the C2 server.[1]"}, {"score": 1, "techniqueID": "T1065", "comment": "Magic Hound malware has communicated with its C2 server over ports 4443 and 3543.[1]"}, {"score": 1, "techniqueID": "T1204", "comment": "Magic Hound has attempted to get users to execute malware via social media and spearphishing emails.[3]"}, {"score": 1, "techniqueID": "T1102", "comment": "Magic Hound malware can use a SOAP Web service to communicate with its C2 server.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Magic Hound", "color": "#66b1ff"}]}