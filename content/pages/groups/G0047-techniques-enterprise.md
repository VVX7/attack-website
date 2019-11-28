Title: enterprise Techniques
Template: general/json
save_as: groups/G0047/G0047-enterprise-layer.json
json: {"description": "Enterprise techniques used by Gamaredon Group, ATT&CK group G0047 v1.0", "name": "Gamaredon Group (G0047)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1025", "comment": "A Gamaredon Group file stealer has the capability to steal data from newly connected logical volumes on a system, including USB drives.[1]"}, {"score": 1, "techniqueID": "T1041", "comment": "A Gamaredon Group file stealer transfers collected files to a hardcoded C2 server.[1]"}, {"score": 1, "techniqueID": "T1120", "comment": "Gamaredon Group tools contained an application to check performance of USB flash drives.[1]"}, {"score": 1, "techniqueID": "T1105", "comment": "Tools used by Gamaredon Group are capable of downloading and executing additional payloads.[1]"}, {"score": 1, "techniqueID": "T1064", "comment": "Gamaredon Group has used various batch scripts to establish C2, download additional files, and conduct other functions.[1]"}, {"score": 1, "techniqueID": "T1071", "comment": "A Gamaredon Group file stealer can communicate over HTTP for C2.[1]"}, {"score": 1, "techniqueID": "T1082", "comment": "A Gamaredon Group file stealer can gather the victim's computer name and drive serial numbers to send to a C2 server.[1]"}, {"score": 1, "techniqueID": "T1033", "comment": "A Gamaredon Group file stealer can gather the victim's username to send to a C2 server.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Gamaredon Group", "color": "#66b1ff"}]}