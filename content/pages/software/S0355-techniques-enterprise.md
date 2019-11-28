Title: enterprise Techniques
Template: general/json
save_as: software/S0355/S0355-enterprise-layer.json
json: {"description": "Enterprise techniques used by Final1stspy, ATT&CK software S0355 v1.0", "name": "Final1stspy (S0355)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1140", "comment": "Final1stspy uses Python code to deobfuscate base64-encoded strings.[1]"}, {"score": 1, "techniqueID": "T1027", "comment": "Final1stspy obfuscates strings with base64 encoding.[1]"}, {"score": 1, "techniqueID": "T1057", "comment": "Final1stspy obtains a list of running processes.[1]"}, {"score": 1, "techniqueID": "T1060", "comment": "Final1stspy creates a Registry Run key to establish persistence.[1]"}, {"score": 1, "techniqueID": "T1071", "comment": "Final1stspy uses HTTP for C2.[1]"}, {"score": 1, "techniqueID": "T1082", "comment": "Final1stspy obtains victim Microsoft Windows version information and CPU architecture.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Final1stspy", "color": "#66b1ff"}]}