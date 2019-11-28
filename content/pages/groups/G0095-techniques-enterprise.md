Title: enterprise Techniques
Template: general/json
save_as: groups/G0095/G0095-enterprise-layer.json
json: {"description": "Enterprise techniques used by Machete, ATT&CK group G0095 v1.0", "name": "Machete (G0095)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1043", "comment": "Machete used TCP port 21 for C2.[1]"}, {"score": 1, "techniqueID": "T1025", "comment": "Machete had a module in its malware to find, encrypt, and upload files from fixed and removable drives.[1]"}, {"score": 1, "techniqueID": "T1074", "comment": "Machete created their own directories to drop files into.[1]"}, {"score": 1, "techniqueID": "T1027", "comment": "Machete employed some visual obfuscation techniques by naming variables as combinations of letters to hinder analysis.[1]"}, {"score": 1, "techniqueID": "T1060", "comment": "Machete used the startup folder for persistence.[1]"}, {"score": 1, "techniqueID": "T1053", "comment": "Machete used scheduled tasks for persistence.[1]"}, {"score": 1, "techniqueID": "T1064", "comment": "Machete used multiple compiled Python scripts on the victim\u2019s system.[1]"}, {"score": 1, "techniqueID": "T1193", "comment": "Machete has delivered spearphishing emails that contain a zipped file with malicious contents.[2][3]"}, {"score": 1, "techniqueID": "T1192", "comment": "Machete has sent phishing emails that contain a link to an external server with ZIP and RAR archives.[1][3]"}, {"score": 1, "techniqueID": "T1071", "comment": "Machete malware used FTP and Python\u2019s urllib library to make HTTP requests to the C2 server.[1]"}, {"score": 1, "techniqueID": "T1032", "comment": "Machete has relied on TLS-encrypted FTP to transfer data out of target environments. [1]"}, {"score": 1, "techniqueID": "T1204", "comment": "Machete has has relied on users opening malicious links or attachments delivered through spearphishing to execute malware.[1][2][3]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Machete", "color": "#66b1ff"}]}