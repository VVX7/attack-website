Title: enterprise Techniques
Template: general/json
save_as: software/S0404/S0404-enterprise-layer.json
json: {"description": "Enterprise techniques used by esentutl, ATT&CK software S0404 v1.0", "name": "esentutl (S0404)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1003", "comment": "esentutl can use Volume Shadow Copy to copy locked files such as ntds.dit.[2][3]"}, {"score": 1, "techniqueID": "T1096", "comment": "esentutl can be used to read and write alternate data streams.[2]"}, {"score": 1, "techniqueID": "T1105", "comment": "esentutl can be used to copy files from a remote host or download files from a given URL.[2]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by esentutl", "color": "#66b1ff"}]}