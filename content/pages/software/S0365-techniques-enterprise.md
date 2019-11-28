Title: enterprise Techniques
Template: general/json
save_as: software/S0365/S0365-enterprise-layer.json
json: {"description": "Enterprise techniques used by Olympic Destroyer, ATT&CK software S0365 v1.1", "name": "Olympic Destroyer (S0365)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1003", "comment": "Olympic Destroyer contains a module that tries to obtain credentials from LSASS, similar to Mimikatz. These credentials are used with PsExec and Windows Management Instrumentation to help the malware propagate itself across a network.[1]"}, {"score": 1, "techniqueID": "T1081", "comment": "Olympic Destroyer contains a module that tries to obtain stored credentials from web browsers.[1]"}, {"score": 1, "techniqueID": "T1485", "comment": "Olympic Destroyer overwrites files locally and on remote shares. [1]"}, {"score": 1, "techniqueID": "T1070", "comment": "Olympic Destroyer will attempt to clear the System and Security event logs using wevtutil.[1]"}, {"score": 1, "techniqueID": "T1490", "comment": "Olympic Destroyer uses the native Windows utilities vssadmin, wbadmin, and bcdedit to delete and disable operating system recovery features such as the Windows backup catalog and Windows Automatic Repair.[1]"}, {"score": 1, "techniqueID": "T1135", "comment": "Olympic Destroyer will attempt to enumerate mapped network shares to later attempt to wipe all files on those shares.[1]"}, {"score": 1, "techniqueID": "T1105", "comment": "Olympic Destroyer attempts to copy itself to remote machines on the network.[1]"}, {"score": 1, "techniqueID": "T1018", "comment": "Olympic Destroyer uses Windows Management Instrumentation to enumerate all systems in the network.[1]"}, {"score": 1, "techniqueID": "T1035", "comment": "Olympic Destroyer utilizes PsExec to help propagate itself across a network.[1]"}, {"score": 1, "techniqueID": "T1489", "comment": "Olympic Destroyer uses the API call ChangeServiceConfigW to disable all services on the affected system.[1]"}, {"score": 1, "techniqueID": "T1016", "comment": "Olympic Destroyer uses API calls to enumerate the infected system's ARP table.[1]"}, {"score": 1, "techniqueID": "T1529", "comment": "Olympic Destroyer will shut down the compromised system after it is done modifying system configuration settings.[1]"}, {"score": 1, "techniqueID": "T1077", "comment": "Olympic Destroyer uses PsExec to interact with the ADMIN$ network share to execute commands on remote systems.[1][2]"}, {"score": 1, "techniqueID": "T1047", "comment": "Olympic Destroyer uses WMI to help propagate itself across a network.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Olympic Destroyer", "color": "#66b1ff"}]}