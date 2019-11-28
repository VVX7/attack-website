Title: enterprise Techniques
Template: general/json
save_as: software/S0084/S0084-enterprise-layer.json
json: {"description": "Enterprise techniques used by Mis-Type, ATT&CK software S0084 v1.0", "name": "Mis-Type (S0084)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1087", "comment": "Mis-Type may create a file containing the results of the command cmd.exe /c net user {{Username}}.[1]"}, {"score": 1, "techniqueID": "T1059", "comment": "Mis-Type uses cmd.exe to run commands for enumerating the host.[1]"}, {"score": 1, "techniqueID": "T1043", "comment": "Mis-Type communicates over common ports such as TCP 80, 443, and 25.[1]"}, {"score": 1, "techniqueID": "T1136", "comment": "Mis-Type may create a temporary user on the system named \"Lost_{{Unique Identifier}}.\"[1]"}, {"score": 1, "techniqueID": "T1094", "comment": "Mis-Type network traffic can communicate over a raw socket.[1]"}, {"score": 1, "techniqueID": "T1132", "comment": "Mis-Type uses Base64 encoding for C2 traffic.[1]"}, {"score": 1, "techniqueID": "T1008", "comment": "Mis-Type first attempts to use a Base64-encoded network protocol over a raw TCP socket for C2, and if that method fails, falls back to a secondary HTTP-based protocol to communicate to an alternate C2 server.[1]"}, {"score": 1, "techniqueID": "T1036", "comment": "Mis-Type saves itself as a file named msdtc.exe, which is also the name of the legitimate Microsoft Distributed Transaction Coordinator service.[1][2]"}, {"score": 1, "techniqueID": "T1071", "comment": "Mis-Type network traffic can communicate over HTTP.[1]"}, {"score": 1, "techniqueID": "T1095", "comment": "Mis-Type network traffic can communicate over a raw socket.[1]"}, {"score": 1, "techniqueID": "T1082", "comment": "The initial beacon packet for Mis-Type contains the operating system version and file system of the victim.[1]"}, {"score": 1, "techniqueID": "T1016", "comment": "Mis-Type may create a file containing the results of the command cmd.exe /c ipconfig /all.[1]"}, {"score": 1, "techniqueID": "T1033", "comment": "Mis-Type runs tests to determine the privilege level of the compromised user.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Mis-Type", "color": "#66b1ff"}]}