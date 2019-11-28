Title: enterprise Techniques
Template: general/json
save_as: groups/G0051/G0051-enterprise-layer.json
json: {"description": "Enterprise techniques used by FIN10, ATT&CK group G0051 v1.1", "name": "FIN10 (G0051)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1107", "comment": "FIN10 has used batch scripts and scheduled tasks to delete critical system files.[1]"}, {"score": 1, "techniqueID": "T1086", "comment": "FIN10 uses PowerShell for execution as well as PowerShell Empire to establish persistence.[1][2]"}, {"score": 1, "techniqueID": "T1060", "comment": "FIN10 has established persistence by using the Registry option in PowerShell Empire to add a Run key.[1][2]"}, {"score": 1, "techniqueID": "T1076", "comment": "FIN10 has used RDP to move laterally to systems in the victim environment.[1]"}, {"score": 1, "techniqueID": "T1105", "comment": "FIN10 has deployed Meterpreter stagers and SplinterRAT instances in the victim network after moving laterally.[1]"}, {"score": 1, "techniqueID": "T1053", "comment": "FIN10 has established persistence by using S4U tasks as well as the Scheduled Task option in PowerShell Empire.[1][2]"}, {"score": 1, "techniqueID": "T1064", "comment": "FIN10 has executed malicious .bat files containing PowerShell commands.[1]"}, {"score": 1, "techniqueID": "T1033", "comment": "FIN10 has used Meterpreter to enumerate users on remote systems.[1]"}, {"score": 1, "techniqueID": "T1078", "comment": "FIN10 has used stolen credentials to connect remotely to victim networks using VPNs protected with only a single factor. The group has also moved laterally using the Local Administrator account.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by FIN10", "color": "#66b1ff"}]}