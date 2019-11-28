Title: enterprise Techniques
Template: general/json
save_as: software/S0180/S0180-enterprise-layer.json
json: {"description": "Enterprise techniques used by Volgmer, ATT&CK software S0180 v1.0", "name": "Volgmer (S0180)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1059", "comment": "Volgmer can execute commands on the victim's machine.[1][2]"}, {"score": 1, "techniqueID": "T1043", "comment": "Some Volgmer variants use ports 8080 and 8000 for C2.[1][2][3]"}, {"score": 1, "techniqueID": "T1094", "comment": "Volgmer uses a custom binary protocol to beacon back to its C2 server. It has also used XOR for encrypting communications.[1][2]"}, {"score": 1, "techniqueID": "T1132", "comment": "Volgmer encodes files before exfiltration.[2]"}, {"score": 1, "techniqueID": "T1140", "comment": "Volgmer deobfuscates its strings and APIs once its executed.[2]"}, {"score": 1, "techniqueID": "T1106", "comment": "Volgmer executes payloads using the Windows API call CreateProcessW().[2]"}, {"score": 1, "techniqueID": "T1083", "comment": "Volgmer can list directories on a victim.[1]"}, {"score": 1, "techniqueID": "T1107", "comment": "Volgmer can delete files and itself after infection to avoid analysis.[2]"}, {"score": 1, "techniqueID": "T1036", "comment": "Some Volgmer variants add new services with display names generated by a list of hard-coded strings such as Application, Background, Security, and Windows, presumably as a way to masquerade as a legitimate service.[2][3]"}, {"score": 1, "techniqueID": "T1031", "comment": "Volgmer installs a copy of itself in a randomly selected service, then overwrites the ServiceDLL entry in the service's Registry entry.[1]"}, {"score": 1, "techniqueID": "T1112", "comment": "Volgmer stores the encoded configuration file in the Registry key HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\WMI\\Security.[2][3]"}, {"score": 1, "techniqueID": "T1050", "comment": "Some Volgmer variants install .dll files as services with names generated by a list of hard-coded strings.[2][3]"}, {"score": 1, "techniqueID": "T1027", "comment": "A Volgmer variant is encoded using a simple XOR cipher.[2]"}, {"score": 1, "techniqueID": "T1057", "comment": "Volgmer can gather a list of processes.[3]"}, {"score": 1, "techniqueID": "T1012", "comment": "Volgmer checks the system for certain Registry keys.[2]"}, {"score": 1, "techniqueID": "T1105", "comment": "Volgmer can download remote files and additional payloads to the victim's machine.[1][2][3]"}, {"score": 1, "techniqueID": "T1032", "comment": "Some Volgmer variants use SSL to encrypt C2 communications.[1]"}, {"score": 1, "techniqueID": "T1082", "comment": "Volgmer can gather system information, the computer name, OS version, drive and serial information from the victim's machine.[1][2][3]"}, {"score": 1, "techniqueID": "T1016", "comment": "Volgmer can gather the IP address from the victim's machine.[3]"}, {"score": 1, "techniqueID": "T1049", "comment": "Volgmer can gather information about TCP connection state.[3]"}, {"score": 1, "techniqueID": "T1007", "comment": "Volgmer queries the system to identify existing services.[1]"}, {"score": 1, "techniqueID": "T1065", "comment": "Some Volgmer variants use port 8088 for C2.[1][2][3]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Volgmer", "color": "#66b1ff"}]}