Title: enterprise Techniques
Template: general/json
save_as: groups/G0069/G0069-enterprise-layer.json
json: {"description": "Enterprise techniques used by MuddyWater, ATT&CK group G0069 v2.1", "name": "MuddyWater (G0069)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1088", "comment": "MuddyWater uses various techniques to bypass UAC.[3]"}, {"score": 1, "techniqueID": "T1191", "comment": "MuddyWater has used CMSTP.exe and a malicious INF to execute its POWERSTATS payload.[4]"}, {"score": 1, "techniqueID": "T1059", "comment": "MuddyWater has used a custom tool for creating reverse shells.[2]"}, {"score": 1, "techniqueID": "T1500", "comment": "MuddyWater has used the .NET csc.exe tool to compile executables from downloaded C# code.[3]"}, {"score": 1, "techniqueID": "T1175", "comment": "MuddyWater has used malware that has the capability to execute malware via COM and Outlook.[6]"}, {"score": 1, "techniqueID": "T1090", "comment": "MuddyWater has controlled POWERSTATS from behind a proxy network to obfuscate the C2 location.[2]"}, {"score": 1, "techniqueID": "T1003", "comment": "MuddyWater has performed credential dumping with Mimikatz, LaZagne, and other tools, including by dumping passwords saved in victim web browsers and email.[1][2]"}, {"score": 1, "techniqueID": "T1503", "comment": "MuddyWater has run a tool that steals passwords saved in victim web browsers.[2]"}, {"score": 1, "techniqueID": "T1081", "comment": "MuddyWater has run a tool that steals passwords saved in victim email.[2]"}, {"score": 1, "techniqueID": "T1002", "comment": "MuddyWater has used the native Windows cabinet creation tool, makecab.exe, likely to compress stolen data to be uploaded.[2]"}, {"score": 1, "techniqueID": "T1140", "comment": "MuddyWater decoded base64-encoded PowerShell commands using a VBS file.[4][7][3]"}, {"score": 1, "techniqueID": "T1173", "comment": "MuddyWater has used malware that can execute PowerShell scripts via DDE.[6]"}, {"score": 1, "techniqueID": "T1083", "comment": "MuddyWater has used malware that checked if the ProgramData folder had folders or files with the keywords \"Kasper,\" \"Panda,\" or \"ESET.\"[6]"}, {"score": 1, "techniqueID": "T1036", "comment": "MuddyWater has used filenames and Registry key names associated with Windows Defender. The group has also stored obfuscated JavaScript code in an image file named temp.jpg.[4][5][3]"}, {"score": 1, "techniqueID": "T1170", "comment": "MuddyWater has used mshta.exe to execute its POWERSTATS payload and to pass a PowerShell one-liner for execution.[4][6]"}, {"score": 1, "techniqueID": "T1104", "comment": "MuddyWater has used one C2 to obtain enumeration scripts and monitor web logs, but a different C2 to send data back. [5]"}, {"score": 1, "techniqueID": "T1027", "comment": "MuddyWater has used Daniel Bohannon\u2019s Invoke-Obfuscation framework. The group has also used other obfuscation methods, including Base64 obfuscation of VBScripts and PowerShell commands.[1][8][1][4][6][5]"}, {"score": 1, "techniqueID": "T1086", "comment": "MuddyWater has used PowerShell for execution.[4][7][6][2][3][5]"}, {"score": 1, "techniqueID": "T1057", "comment": "MuddyWater has used malware to obtain a list of running processes on the system.[6]"}, {"score": 1, "techniqueID": "T1060", "comment": "MuddyWater has added Registry Run key KCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\SystemTextEncoding to establish persistence.[4][6][5]"}, {"score": 1, "techniqueID": "T1105", "comment": "MuddyWater has used malware that can upload additional files to the victim\u2019s machine.[6][3]"}, {"score": 1, "techniqueID": "T1085", "comment": "MuddyWater has used malware that leveraged rundll32.exe in a Registry Run key to execute a .dll.[6]"}, {"score": 1, "techniqueID": "T1113", "comment": "MuddyWater has used malware that can capture screenshots of the victim\u2019s machine.[6]"}, {"score": 1, "techniqueID": "T1064", "comment": "MuddyWater has used VBScript and JavaScript files to execute its POWERSTATS payload. MuddyWater has also used Microsoft scriptlets, macros, and PowerShell scripts.[[4][7][6][2][3]"}, {"score": 1, "techniqueID": "T1063", "comment": "MuddyWater has used malware to check running processes against a hard-coded list of security tools often used by malware researchers.[6]"}, {"score": 1, "techniqueID": "T1193", "comment": "MuddyWater has compromised third parties and used compromised accounts to send spearphishing emails with targeted attachments to recipients.[1][4][6]"}, {"score": 1, "techniqueID": "T1082", "comment": "MuddyWater has used malware that can collect the victim\u2019s OS version and machine name.[6][5]"}, {"score": 1, "techniqueID": "T1016", "comment": "MuddyWater has used malware to collect the victim\u2019s IP address and domain name.[6]"}, {"score": 1, "techniqueID": "T1033", "comment": "MuddyWater has used malware that can collect the victim\u2019s username.[6]"}, {"score": 1, "techniqueID": "T1204", "comment": "MuddyWater has attempted to get users to enable macros and launch malicious Microsoft Word documents delivered via spearphishing emails.[1][4][6][5]"}, {"score": 1, "techniqueID": "T1047", "comment": "MuddyWater has used malware that leveraged WMI for execution and querying host information.[6][3][5]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by MuddyWater", "color": "#66b1ff"}]}