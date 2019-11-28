Title: enterprise Techniques
Template: general/json
save_as: software/S0370/S0370-enterprise-layer.json
json: {"description": "Enterprise techniques used by SamSam, ATT&CK software S0370 v1.0", "name": "SamSam (S0370)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1009", "comment": "SamSam has used garbage code to pad some of its malware components.[3]"}, {"score": 1, "techniqueID": "T1486", "comment": "SamSam encrypts victim files using RSA-2048 encryption and demands a ransom be paid in Bitcoin to decrypt those files.[3]"}, {"score": 1, "techniqueID": "T1107", "comment": "SamSam has been seen deleting its own files and payloads to make analysis of the attack more difficult.[3]"}, {"score": 1, "techniqueID": "T1027", "comment": "SamSam has been seen using AES or DES to encrypt payloads and payload components.[3][2]"}, {"score": 1, "techniqueID": "T1064", "comment": "SamSam uses custom batch scripts to execute some of its components.[3]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by SamSam", "color": "#66b1ff"}]}