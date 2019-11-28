Title: enterprise Techniques
Template: general/json
save_as: groups/G0090/G0090-enterprise-layer.json
json: {"description": "Enterprise techniques used by WIRTE, ATT&CK group G0090 v1.0", "name": "WIRTE (G0090)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1140", "comment": "WIRTE has decoded a base64 encoded document which was embedded in a VBS script.[1]"}, {"score": 1, "techniqueID": "T1086", "comment": "WIRTE has used PowerShell for script execution.[1]"}, {"score": 1, "techniqueID": "T1117", "comment": "WIRTE has used Regsvr32.exe to trigger the execution of a malicious script.[1]"}, {"score": 1, "techniqueID": "T1105", "comment": "WIRTE has downloaded PowerShell code from the C2 server to be executed.[1]"}, {"score": 1, "techniqueID": "T1064", "comment": "WIRTE has used VBS and PowerShell scripts throughout its operation.    [1]"}, {"score": 1, "techniqueID": "T1071", "comment": "WIRTE has used HTTP for network communication. [1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by WIRTE", "color": "#66b1ff"}]}