Title: enterprise Techniques
Template: general/json
save_as: software/S0373/S0373-enterprise-layer.json
json: {"description": "Enterprise techniques used by Astaroth, ATT&CK software S0373 v1.1", "name": "Astaroth (S0373)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1115", "comment": "Astaroth collects information from the clipboard by using the OpenClipboard() and GetClipboardData() libraries.[1]"}, {"score": 1, "techniqueID": "T1059", "comment": "Astaroth spawns a CMD process to execute commands.[1]"}, {"score": 1, "techniqueID": "T1223", "comment": "Astaroth uses ActiveX objects for file execution and manipulation.[2]"}, {"score": 1, "techniqueID": "T1003", "comment": "Astaroth uses an external software known as NetPass to recover passwords.[1]"}, {"score": 1, "techniqueID": "T1132", "comment": "Astaroth encodes data using Base64 before sending it to the C2 server.[2]"}, {"score": 1, "techniqueID": "T1074", "comment": "Astaroth collects data in a plaintext file named r1.log before exfiltration.[2]"}, {"score": 1, "techniqueID": "T1140", "comment": "Astaroth uses a fromCharCode() deobfuscation method to avoid explicitly writing execution commands and to hide its code.[1]"}, {"score": 1, "techniqueID": "T1129", "comment": "Astaroth uses the LoadLibraryExW() function to load additional modules.[1]"}, {"score": 1, "techniqueID": "T1041", "comment": "Astaroth exfiltrates collected information from its r1.log file to the external C2 server.[1]"}, {"score": 1, "techniqueID": "T1143", "comment": "Astaroth loads its module with the XSL script parameter vShow set to zero, which opens the application with a hidden window.[1]"}, {"score": 1, "techniqueID": "T1056", "comment": "Astaroth logs keystrokes from the victim's machine.[2]"}, {"score": 1, "techniqueID": "T1027", "comment": "Astaroth obfuscates its JScript code.[1]"}, {"score": 1, "techniqueID": "T1057", "comment": "Astaroth searches for different processes on the system.[1]"}, {"score": 1, "techniqueID": "T1093", "comment": "Astaroth searches for unins000.exe (GAS Tecnologia software), Syswow64\\userinit.exe or System32\\userinit.exe to evasively create a new process in suspended state.[1]"}, {"score": 1, "techniqueID": "T1060", "comment": "Astaroth creates a startup item for persistence.[2]"}, {"score": 1, "techniqueID": "T1117", "comment": "Astaroth can be loaded through regsvr32.exe.[1]"}, {"score": 1, "techniqueID": "T1105", "comment": "Astaroth uses certutil and BITSAdmin to download additional malware.[2][1]"}, {"score": 1, "techniqueID": "T1064", "comment": "Astaroth uses JavaScript to perform its core functionalities.[2]"}, {"score": 1, "techniqueID": "T1063", "comment": "Astaroth checks for the presence of Avast antivirus in the C:\\Program\\Files\\ folder.[2]"}, {"score": 1, "techniqueID": "T1023", "comment": "Astaroth's initial payload is a malicious .LNK file.(Citation :Cybereason Astaroth Feb 2019)[2]"}, {"score": 1, "techniqueID": "T1045", "comment": "Astaroth uses a software packer called Pe123\\RPolyCryptor.[1]"}, {"score": 1, "techniqueID": "T1082", "comment": "Astaroth collects the machine name and keyboard language from the system.[2][1]"}, {"score": 1, "techniqueID": "T1016", "comment": "Astaroth collects the external IP address from the system.[2]"}, {"score": 1, "techniqueID": "T1124", "comment": "Astaroth collects the timestamp from the infected machine.[2]"}, {"score": 1, "techniqueID": "T1047", "comment": "Astaroth uses WMIC to execute payloads.[2]"}, {"score": 1, "techniqueID": "T1220", "comment": "Astaroth executes embedded JScript or VBScript in an XSL stylesheet located on a remote domain.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Astaroth", "color": "#66b1ff"}]}