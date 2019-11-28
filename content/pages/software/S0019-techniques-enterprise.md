Title: enterprise Techniques
Template: general/json
save_as: software/S0019/S0019-enterprise-layer.json
json: {"description": "Enterprise techniques used by Regin, ATT&CK software S0019 v1.0", "name": "Regin (S0019)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1116", "comment": "Regin stage 1 modules for 64-bit systems have been found to be signed with fake certificates masquerading as originating from Microsoft Corporation and Broadcom Corporation.[1]"}, {"score": 1, "techniqueID": "T1090", "comment": "Regin leveraged several compromised universities as proxies to obscure its origin.[1]"}, {"score": 1, "techniqueID": "T1094", "comment": "The Regin malware platform can use ICMP to communicate between infected computers.[1]"}, {"score": 1, "techniqueID": "T1056", "comment": "Regin contains a keylogger.[1]"}, {"score": 1, "techniqueID": "T1112", "comment": "Regin appears to have functionality to modify remote Registry information.[1]"}, {"score": 1, "techniqueID": "T1040", "comment": "Regin appears to have functionality to sniff for credentials passed over HTTP, SMTP, and SMB.[1]"}, {"score": 1, "techniqueID": "T1096", "comment": "The Regin malware platform uses Extended Attributes to store encrypted executables.[1]"}, {"score": 1, "techniqueID": "T1071", "comment": "The Regin malware platform supports many standard protocols, including HTTP, HTTPS, and SMB.[1]"}, {"score": 1, "techniqueID": "T1095", "comment": "The Regin malware platform can use ICMP to communicate between infected computers.[1]"}, {"score": 1, "techniqueID": "T1077", "comment": "The Regin malware platform can use Windows admin shares to move laterally.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Regin", "color": "#66b1ff"}]}