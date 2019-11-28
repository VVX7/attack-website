Title: enterprise Techniques
Template: general/json
save_as: software/S0142/S0142-enterprise-layer.json
json: {"description": "Enterprise techniques used by StreamEx, ATT&CK software S0142 v1.0", "name": "StreamEx (S0142)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1059", "comment": "StreamEx has the ability to remotely execute commands.[1]"}, {"score": 1, "techniqueID": "T1083", "comment": "StreamEx has the ability to enumerate drive types.[1]"}, {"score": 1, "techniqueID": "T1112", "comment": "StreamEx has the ability to modify the Registry.[1]"}, {"score": 1, "techniqueID": "T1050", "comment": "StreamEx establishes persistence by installing a new service pointing to its DLL and setting the service to auto-start.[1]"}, {"score": 1, "techniqueID": "T1027", "comment": "StreamEx obfuscates some commands by using statically programmed fragments of strings when starting a DLL. It also uses a one-byte xor against 0x91 to encode configuration data.[1]"}, {"score": 1, "techniqueID": "T1057", "comment": "StreamEx has the ability to enumerate processes.[1]"}, {"score": 1, "techniqueID": "T1085", "comment": "StreamEx uses rundll32 to call an exported function.[1]"}, {"score": 1, "techniqueID": "T1063", "comment": "StreamEx has the ability to scan for security tools such as firewalls and antivirus tools.[1]"}, {"score": 1, "techniqueID": "T1082", "comment": "StreamEx has the ability to enumerate system information.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by StreamEx", "color": "#66b1ff"}]}