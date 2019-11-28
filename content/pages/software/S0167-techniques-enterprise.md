Title: enterprise Techniques
Template: general/json
save_as: software/S0167/S0167-enterprise-layer.json
json: {"description": "Enterprise techniques used by Matroyshka, ATT&CK software S0167 v1.0", "name": "Matroyshka (S0167)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1059", "comment": "Matroyshka is capable of providing Meterpreter shell access.[1]"}, {"score": 1, "techniqueID": "T1003", "comment": "Matroyshka is capable of stealing Outlook passwords.[1][2]"}, {"score": 1, "techniqueID": "T1056", "comment": "Matroyshka is capable of keylogging.[1][2]"}, {"score": 1, "techniqueID": "T1027", "comment": "Matroyshka obfuscates API function names using a substitute cipher combined with Base64 encoding.[2]"}, {"score": 1, "techniqueID": "T1055", "comment": "Matroyshka uses reflective DLL injection to inject the malicious library and execute the RAT.[2]"}, {"score": 1, "techniqueID": "T1060", "comment": "Matroyshka can establish persistence by adding Registry Run keys.[1][2]"}, {"score": 1, "techniqueID": "T1085", "comment": "Matroyshka uses rundll32.exe in a Registry Run key value for execution as part of its persistence mechanism.[2]"}, {"score": 1, "techniqueID": "T1053", "comment": "Matroyshka can establish persistence by adding a Scheduled Task named \"Microsoft Boost Kernel Optimization\".[1][2]"}, {"score": 1, "techniqueID": "T1113", "comment": "Matroyshka is capable of performing screen captures.[1][2]"}, {"score": 1, "techniqueID": "T1071", "comment": "Matroyshka uses DNS for C2.[1][2]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Matroyshka", "color": "#66b1ff"}]}