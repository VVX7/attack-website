Title: enterprise Techniques
Template: general/json
save_as: software/S0132/S0132-enterprise-layer.json
json: {"description": "Enterprise techniques used by H1N1, ATT&CK software S0132 v1.1", "name": "H1N1 (S0132)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1088", "comment": "H1N1 bypasses user access control by using a DLL hijacking vulnerability in the Windows Update Standalone Installer (wusa.exe).[2]"}, {"score": 1, "techniqueID": "T1059", "comment": "H1N1 kills and disables services by using cmd.exe.[2]"}, {"score": 1, "techniqueID": "T1003", "comment": "H1N1 dumps usernames and passwords from Firefox, Internet Explorer, and Outlook.[2]"}, {"score": 1, "techniqueID": "T1001", "comment": "H1N1 obfuscates C2 traffic with an altered version of base64.[2]"}, {"score": 1, "techniqueID": "T1089", "comment": "H1N1 kills and disables services for Windows Firewall, Windows Security Center, and Windows Defender.[2]"}, {"score": 1, "techniqueID": "T1490", "comment": "H1N1 disable recovery options and deletes shadow copies from the victim.[2]"}, {"score": 1, "techniqueID": "T1027", "comment": "H1N1 uses multiple techniques to obfuscate strings, including XOR.[1]"}, {"score": 1, "techniqueID": "T1105", "comment": "H1N1 contains a command to download and execute a file from a remotely hosted URL using WinINet HTTP requests.[2]"}, {"score": 1, "techniqueID": "T1091", "comment": "H1N1 has functionality to copy itself to removable media.[2]"}, {"score": 1, "techniqueID": "T1045", "comment": "H1N1 uses a custom packing algorithm.[1]"}, {"score": 1, "techniqueID": "T1032", "comment": "H1N1 encrypts C2 traffic using an RC4 key.[2]"}, {"score": 1, "techniqueID": "T1080", "comment": "H1N1 has functionality to copy itself to network shares.[2]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by H1N1", "color": "#66b1ff"}]}