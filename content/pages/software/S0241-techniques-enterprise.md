Title: enterprise Techniques
Template: general/json
save_as: software/S0241/S0241-enterprise-layer.json
json: {"description": "Enterprise techniques used by RATANKBA, ATT&CK software S0241 v1.0", "name": "RATANKBA (S0241)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1087", "comment": "RATANKBA uses the net user command.[2]"}, {"score": 1, "techniqueID": "T1059", "comment": "RATANKBA uses cmd.exe to execute commands.[1][2]"}, {"score": 1, "techniqueID": "T1043", "comment": "RATANKBA uses port 443 for C2.[2]"}, {"score": 1, "techniqueID": "T1086", "comment": "There is a variant of RATANKBA that uses a PowerShell script instead of the traditional PE form.[1][2]"}, {"score": 1, "techniqueID": "T1057", "comment": "RATANKBA lists the system\u2019s processes.[1][2]"}, {"score": 1, "techniqueID": "T1055", "comment": "RATANKBA performs a reflective DLL injection using a given pid.[1][2]"}, {"score": 1, "techniqueID": "T1012", "comment": "RATANKBA uses the command reg query \"HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\InternetSettings\".[2]"}, {"score": 1, "techniqueID": "T1105", "comment": "RATANKBA uploads and downloads information.[1][2]"}, {"score": 1, "techniqueID": "T1018", "comment": "RATANKBA runs the net view /domain and net view commands.[2]"}, {"score": 1, "techniqueID": "T1071", "comment": "RATANKBA uses HTTP/HTTPS for command and control communication.[1][2]"}, {"score": 1, "techniqueID": "T1082", "comment": "RATANKBA gathers information about the OS architecture, OS name, and OS version/Service pack.[1][2]"}, {"score": 1, "techniqueID": "T1016", "comment": "RATANKBA gathers the victim\u2019s IP address via the ipconfig -all command.[1][2]"}, {"score": 1, "techniqueID": "T1049", "comment": "RATANKBA uses netstat -ano to search for specific IP address ranges.[2]"}, {"score": 1, "techniqueID": "T1033", "comment": "RATANKBA runs the whoami and query user commands.[2]"}, {"score": 1, "techniqueID": "T1007", "comment": "RATANKBA uses tasklist /svc to display running tasks.[2]"}, {"score": 1, "techniqueID": "T1047", "comment": "RATANKBA uses WMI to perform process monitoring.[1][2]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by RATANKBA", "color": "#66b1ff"}]}