Title: enterprise Techniques
Template: general/json
save_as: software/S0165/S0165-enterprise-layer.json
json: {"description": "Enterprise techniques used by OSInfo, ATT&CK software S0165 v1.0", "name": "OSInfo (S0165)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1087", "comment": "OSInfo enumerates local and domain users[1]"}, {"score": 1, "techniqueID": "T1135", "comment": "OSInfo discovers shares on the network[1]"}, {"score": 1, "techniqueID": "T1069", "comment": "OSInfo specifically looks for Domain Admins, Power Users, and the Administrators groups within the domain and locally[1]"}, {"score": 1, "techniqueID": "T1012", "comment": "OSInfo queries the registry to look for information about Terminal Services.[1]"}, {"score": 1, "techniqueID": "T1018", "comment": "OSInfo performs a connection test to discover remote systems in the network[1]"}, {"score": 1, "techniqueID": "T1082", "comment": "OSInfo discovers information about the infected machine.[1]"}, {"score": 1, "techniqueID": "T1016", "comment": "OSInfo discovers the current domain information.[1]"}, {"score": 1, "techniqueID": "T1049", "comment": "OSInfo enumerates the current network connections similar to  net use .[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by OSInfo", "color": "#66b1ff"}]}