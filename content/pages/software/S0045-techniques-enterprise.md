Title: enterprise Techniques
Template: general/json
save_as: software/S0045/S0045-enterprise-layer.json
json: {"description": "Enterprise techniques used by ADVSTORESHELL, ATT&CK software S0045 v1.0", "name": "ADVSTORESHELL (S0045)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1059", "comment": "ADVSTORESHELL can create a remote shell and run a given command.[2][3]"}, {"score": 1, "techniqueID": "T1043", "comment": "A variant of ADVSTORESHELL attempts communication to the C2 server over HTTP on port 443.[3]"}, {"score": 1, "techniqueID": "T1122", "comment": "Some variants of ADVSTORESHELL achieve persistence by registering the payload as a Shell Icon Overlay handler COM object.[2]"}, {"score": 1, "techniqueID": "T1002", "comment": "ADVSTORESHELL compresses output data generated by command execution with a custom implementation of the Lempel\u2013Ziv\u2013Welch (LZW) algorithm.[2]"}, {"score": 1, "techniqueID": "T1132", "comment": "C2 traffic from ADVSTORESHELL is encrypted, then encoded with Base64 encoding.[1]"}, {"score": 1, "techniqueID": "T1022", "comment": "ADVSTORESHELL encrypts with the 3DES algorithm and a hardcoded key prior to exfiltration.[2]"}, {"score": 1, "techniqueID": "T1074", "comment": "ADVSTORESHELL stores output from command execution in a .dat file in the %TEMP% directory.[2]"}, {"score": 1, "techniqueID": "T1106", "comment": "ADVSTORESHELL is capable of starting a process using CreateProcess.[3]"}, {"score": 1, "techniqueID": "T1041", "comment": "ADVSTORESHELL exfiltrates data over the same channel used for C2.[2]"}, {"score": 1, "techniqueID": "T1083", "comment": "ADVSTORESHELL can list files and directories.[2][3]"}, {"score": 1, "techniqueID": "T1107", "comment": "ADVSTORESHELL can delete files and directories.[2]"}, {"score": 1, "techniqueID": "T1056", "comment": "ADVSTORESHELL can perform keylogging.[2][3]"}, {"score": 1, "techniqueID": "T1112", "comment": "ADVSTORESHELL is capable of setting and deleting Registry values.[3]"}, {"score": 1, "techniqueID": "T1027", "comment": "Most of the strings in ADVSTORESHELL are encrypted with an XOR-based algorithm; some strings are also encrypted with 3DES and reversed. API function names are also reversed, presumably to avoid detection in memory.[1][3]"}, {"score": 1, "techniqueID": "T1120", "comment": "ADVSTORESHELL can list connected devices.[2]"}, {"score": 1, "techniqueID": "T1057", "comment": "ADVSTORESHELL can list running processes.[2]"}, {"score": 1, "techniqueID": "T1012", "comment": "ADVSTORESHELL can enumerate registry keys.[2][3]"}, {"score": 1, "techniqueID": "T1060", "comment": "ADVSTORESHELL achieves persistence by adding itself to the HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run Registry key.[1][2][3]"}, {"score": 1, "techniqueID": "T1085", "comment": "ADVSTORESHELL has used rundll32.exe in a Registry value to establish persistence.[3]"}, {"score": 1, "techniqueID": "T1029", "comment": "ADVSTORESHELL collects, compresses, encrypts, and exfiltrates data to the C2 server every 10 minutes.[2]"}, {"score": 1, "techniqueID": "T1071", "comment": "ADVSTORESHELL connects to port 80 of a C2 server using Wininet API.[1]"}, {"score": 1, "techniqueID": "T1032", "comment": "A variant of ADVSTORESHELL encrypts some C2 with 3DES and RSA.[3]"}, {"score": 1, "techniqueID": "T1082", "comment": "ADVSTORESHELL can run Systeminfo to gather information about the victim.[2][3]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by ADVSTORESHELL", "color": "#66b1ff"}]}