Title: enterprise Techniques
Template: general/json
save_as: software/S0335/S0335-enterprise-layer.json
json: {"description": "Enterprise techniques used by Carbon, ATT&CK software S0335 v1.0", "name": "Carbon (S0335)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1087", "comment": "Carbon runs the net group command to list accounts on the system.[3]"}, {"score": 1, "techniqueID": "T1043", "comment": "Carbon uses port 80 for C2 communications.[1]"}, {"score": 1, "techniqueID": "T1074", "comment": "Carbon creates a base directory that contains the files and folders that are collected.[1]"}, {"score": 1, "techniqueID": "T1140", "comment": "Carbon decrypts task and configuration files for execution.[1]"}, {"score": 1, "techniqueID": "T1048", "comment": "Carbon uses HTTP to send data to the C2 server.[1]"}, {"score": 1, "techniqueID": "T1050", "comment": "Carbon establishes persistence by creating a service and naming it based off the operating system version running on the current machine.[1]"}, {"score": 1, "techniqueID": "T1027", "comment": "Carbon encrypts configuration files and tasks for the malware to complete using CAST-128 algorithm.[1]"}, {"score": 1, "techniqueID": "T1057", "comment": "Carbon can list the processes on the victim\u2019s machine.[1]"}, {"score": 1, "techniqueID": "T1055", "comment": "Carbon has a command to inject code into a process.[1]"}, {"score": 1, "techniqueID": "T1012", "comment": "Carbon enumerates values in the Registry.[1]"}, {"score": 1, "techniqueID": "T1018", "comment": "Carbon uses the net view command.[3]"}, {"score": 1, "techniqueID": "T1053", "comment": "Carbon creates several tasks for later execution to continue persistence on the victim\u2019s machine.[1]"}, {"score": 1, "techniqueID": "T1095", "comment": "Carbon uses TCP and UDP for C2.[1]"}, {"score": 1, "techniqueID": "T1016", "comment": "Carbon can collect the IP address of the victims and other computers on the network using the commands: ipconfig -all nbtstat -n, and nbtstat -s.[1][3]"}, {"score": 1, "techniqueID": "T1049", "comment": "Carbon uses the netstat -r and netstat -an commands.[3]"}, {"score": 1, "techniqueID": "T1124", "comment": "Carbon uses the command net time \\127.0.0.1 to get information the system\u2019s time.[3]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Carbon", "color": "#66b1ff"}]}