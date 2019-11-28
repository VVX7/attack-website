Title: enterprise Techniques
Template: general/json
save_as: software/S0228/S0228-enterprise-layer.json
json: {"description": "Enterprise techniques used by NanHaiShu, ATT&CK software S0228 v1.0", "name": "NanHaiShu (S0228)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1089", "comment": "NanHaiShu can change Internet Explorer settings to reduce warnings about malware activity.[1]"}, {"score": 1, "techniqueID": "T1107", "comment": "NanHaiShu launches a script to delete their original decoy file to cover tracks.[2]"}, {"score": 1, "techniqueID": "T1170", "comment": "NanHaiShu uses mshta.exe to load its program and files.[2]"}, {"score": 1, "techniqueID": "T1027", "comment": "NanHaiShu encodes files in Base64.[2]"}, {"score": 1, "techniqueID": "T1060", "comment": "NanHaiShu modifies the %regrun% Registry to point itself to an autostart mechanism.[2]"}, {"score": 1, "techniqueID": "T1105", "comment": "NanHaiShu can download additional files from URLs.[1]"}, {"score": 1, "techniqueID": "T1064", "comment": "NanHaiShu executes additional Jscript and VBScript code on the victim's machine.[2]"}, {"score": 1, "techniqueID": "T1071", "comment": "NanHaiShu uses DNS for the C2 communications.[2]"}, {"score": 1, "techniqueID": "T1082", "comment": "NanHaiShu can gather the victim computer name and serial number.[1]"}, {"score": 1, "techniqueID": "T1016", "comment": "NanHaiShu can gather information about the victim proxy server.[1]"}, {"score": 1, "techniqueID": "T1033", "comment": "NanHaiShu collects the username from the victim.[2]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by NanHaiShu", "color": "#66b1ff"}]}