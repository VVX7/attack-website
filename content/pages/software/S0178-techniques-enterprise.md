Title: enterprise Techniques
Template: general/json
save_as: software/S0178/S0178-enterprise-layer.json
json: {"description": "Enterprise techniques used by Truvasys, ATT&CK software S0178 v1.0", "name": "Truvasys (S0178)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1036", "comment": "To establish persistence, Truvasys adds a Registry Run key with a value \"TaskMgr\" in an attempt to masquerade as the legitimate Windows Task Manager.[1]"}, {"score": 1, "techniqueID": "T1060", "comment": "Truvasys adds a Registry Run key to establish persistence.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Truvasys", "color": "#66b1ff"}]}