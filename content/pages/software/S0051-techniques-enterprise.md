Title: enterprise Techniques
Template: general/json
save_as: software/S0051/S0051-enterprise-layer.json
json: {"description": "Enterprise techniques used by MiniDuke, ATT&CK software S0051 v1.0", "name": "MiniDuke (S0051)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1008", "comment": "MiniDuke uses Google Search to identify C2 servers if its primary C2 method via Twitter is not working.[2]"}, {"score": 1, "techniqueID": "T1105", "comment": "MiniDuke can download additional encrypted backdoors onto the victim via GIF files.[2]"}, {"score": 1, "techniqueID": "T1071", "comment": "MiniDuke uses HTTP and HTTPS for command and control.[1]"}, {"score": 1, "techniqueID": "T1102", "comment": "Some MiniDuke components use Twitter to initially obtain the address of a C2 server or as a backup if no hard-coded C2 server responds.[1][2]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by MiniDuke", "color": "#66b1ff"}]}