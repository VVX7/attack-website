Title: enterprise Techniques
Template: general/json
save_as: software/S0219/S0219-enterprise-layer.json
json: {"description": "Enterprise techniques used by WINERACK, ATT&CK software S0219 v1.0", "name": "WINERACK (S0219)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1010", "comment": "WINERACK can enumerate active windows.[1]"}, {"score": 1, "techniqueID": "T1059", "comment": "WINERACK can create a reverse shell that utilizes statically-linked Wine cmd.exe code to emulate Windows command prompt commands.[1]"}, {"score": 1, "techniqueID": "T1083", "comment": "WINERACK can enumerate files and directories.[1]"}, {"score": 1, "techniqueID": "T1057", "comment": "WINERACK can enumerate processes.[1]"}, {"score": 1, "techniqueID": "T1082", "comment": "WINERACK can gather information about the host.[1]"}, {"score": 1, "techniqueID": "T1033", "comment": "WINERACK can gather information on the victim username.[1]"}, {"score": 1, "techniqueID": "T1007", "comment": "WINERACK can enumerate services.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by WINERACK", "color": "#66b1ff"}]}