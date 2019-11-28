Title: enterprise Techniques
Template: general/json
save_as: software/S0105/S0105-enterprise-layer.json
json: {"description": "Enterprise techniques used by dsquery, ATT&CK software S0105 v1.1", "name": "dsquery (S0105)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1087", "comment": "dsquery can be used to gather information on user accounts within a domain.[1]"}, {"score": 1, "techniqueID": "T1482", "comment": "dsquery can be used to gather information on domain trusts with dsquery * -filter \"(objectClass=trustedDomain)\" -attr *.[2]"}, {"score": 1, "techniqueID": "T1069", "comment": "dsquery can be used to gather information on permission groups within a domain.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by dsquery", "color": "#66b1ff"}]}