Title: enterprise Techniques
Template: general/json
save_as: groups/G0062/G0062-enterprise-layer.json
json: {"description": "Enterprise techniques used by TA459, ATT&CK group G0062 v1.0", "name": "TA459 (G0062)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1203", "comment": "TA459 has exploited Microsoft Word vulnerability CVE-2017-0199 for execution.[1]"}, {"score": 1, "techniqueID": "T1086", "comment": "TA459 has used PowerShell for execution of a payload.[1]"}, {"score": 1, "techniqueID": "T1064", "comment": "TA459 has a VBScript for execution.[1]"}, {"score": 1, "techniqueID": "T1193", "comment": "TA459 has targeted victims using spearphishing emails with malicious Microsoft Word attachments.[1]"}, {"score": 1, "techniqueID": "T1204", "comment": "TA459 has attempted to get victims to open malicious Microsoft Word attachment sent via spearphishing.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by TA459", "color": "#66b1ff"}]}