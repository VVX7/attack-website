Title: enterprise Techniques
Template: general/json
save_as: groups/G0008/G0008-enterprise-layer.json
json: {"description": "Enterprise techniques used by Carbanak, ATT&CK group G0008 v1.0", "name": "Carbanak (G0008)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1089", "comment": "Carbanak may use netsh to add local firewall rule exceptions.[4]"}, {"score": 1, "techniqueID": "T1036", "comment": "Carbanak malware names itself \"svchost.exe,\" which is the name of the Windows shared service host program.[1]"}, {"score": 1, "techniqueID": "T1050", "comment": "Carbanak malware installs itself as a service to provide persistence and SYSTEM privileges.[1]"}, {"score": 1, "techniqueID": "T1219", "comment": "Carbanak used legitimate programs such as AmmyAdmin and Team Viewer for remote interactive C2 to target systems.[4]"}, {"score": 1, "techniqueID": "T1085", "comment": "Carbanak installs VNC server software that executes through rundll32.[1]"}, {"score": 1, "techniqueID": "T1078", "comment": "Carbanak actors used legitimate credentials of banking employees to perform operations that sent them millions of dollars.[1]"}, {"score": 1, "techniqueID": "T1102", "comment": "Carbanak has used a VBScript named \"ggldr\" that uses Google Apps Script, Sheets, and Forms services for C2.[3]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Carbanak", "color": "#66b1ff"}]}