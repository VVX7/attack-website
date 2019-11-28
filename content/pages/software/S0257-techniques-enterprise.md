Title: enterprise Techniques
Template: general/json
save_as: software/S0257/S0257-enterprise-layer.json
json: {"description": "Enterprise techniques used by VERMIN, ATT&CK software S0257 v1.0", "name": "VERMIN (S0257)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1123", "comment": "VERMIN can perform audio capture.[1]"}, {"score": 1, "techniqueID": "T1119", "comment": "VERMIN saves each collected file with the automatically generated format {{0:dd-MM-yyyy}}.txt .[1]"}, {"score": 1, "techniqueID": "T1115", "comment": "VERMIN collects data stored in the clipboard.[1]"}, {"score": 1, "techniqueID": "T1022", "comment": "VERMIN encrypts the collected files using 3-DES.[1]"}, {"score": 1, "techniqueID": "T1140", "comment": "VERMIN decrypts code, strings, and commands to use once it's on the victim's machine.[1]"}, {"score": 1, "techniqueID": "T1107", "comment": "VERMIN can delete files on the victim\u2019s machine.[1]"}, {"score": 1, "techniqueID": "T1056", "comment": "VERMIN collects keystrokes from the victim machine.[1]"}, {"score": 1, "techniqueID": "T1027", "comment": "VERMIN is obfuscated using the obfuscation tool called ConfuserEx.[1]"}, {"score": 1, "techniqueID": "T1057", "comment": "VERMIN can get a list of the processes and running tasks on the system.[1]"}, {"score": 1, "techniqueID": "T1105", "comment": "VERMIN can download and upload files to the victim's machine.[1]"}, {"score": 1, "techniqueID": "T1113", "comment": "VERMIN can perform screen captures of the victim\u2019s machine.[1]"}, {"score": 1, "techniqueID": "T1063", "comment": "VERMIN uses WMI to check for anti-virus software installed on the system.[1]"}, {"score": 1, "techniqueID": "T1045", "comment": "VERMIN is initially packed.[1]"}, {"score": 1, "techniqueID": "T1071", "comment": "VERMIN uses HTTP for C2 communications.[1]"}, {"score": 1, "techniqueID": "T1082", "comment": "VERMIN collects the OS name, machine name, and architecture information.[1]"}, {"score": 1, "techniqueID": "T1016", "comment": "VERMIN gathers the local IP address.[1]"}, {"score": 1, "techniqueID": "T1033", "comment": "VERMIN gathers the username from the victim\u2019s machine.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by VERMIN", "color": "#66b1ff"}]}