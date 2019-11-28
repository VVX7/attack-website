Title: enterprise Techniques
Template: general/json
save_as: software/S0201/S0201-enterprise-layer.json
json: {"description": "Enterprise techniques used by JPIN, ATT&CK software S0201 v1.0", "name": "JPIN (S0201)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1197", "comment": "A JPIN variant downloads the backdoor payload via the BITS service.[1]"}, {"score": 1, "techniqueID": "T1059", "comment": "JPIN can use the command-line utility cacls.exe to change file permissions.[1]"}, {"score": 1, "techniqueID": "T1089", "comment": "JPIN lower disable security settings by changing Registry keys.[1]"}, {"score": 1, "techniqueID": "T1083", "comment": "JPIN can enumerate drives and their types. It can also change file permissions using cacls.exe.[1]"}, {"score": 1, "techniqueID": "T1222", "comment": "JPIN can use the command-line utility cacls.exe to change file permissions.[1]"}, {"score": 1, "techniqueID": "T1107", "comment": "JPIN's installer/uninstaller component deletes itself if it encounters a version of Windows earlier than Windows XP or identifies security-related processes running.[1]"}, {"score": 1, "techniqueID": "T1056", "comment": "JPIN contains a custom keylogger.[1]"}, {"score": 1, "techniqueID": "T1027", "comment": "A JPIN uses a encrypted and compressed payload that is disguised as a bitmap within the resource section of the installer.[1]"}, {"score": 1, "techniqueID": "T1069", "comment": "JPIN can obtain the victim user name.[1]"}, {"score": 1, "techniqueID": "T1057", "comment": "JPIN can list running processes.[1]"}, {"score": 1, "techniqueID": "T1055", "comment": "JPIN can inject content into lsass.exe to load a module.[1]"}, {"score": 1, "techniqueID": "T1012", "comment": "JPIN can enumerate Registry keys.[1]"}, {"score": 1, "techniqueID": "T1105", "comment": "JPIN can download files and upgrade itself.[1]"}, {"score": 1, "techniqueID": "T1063", "comment": "JPIN checks for the presence of certain security-related processes and deletes its installer/uninstaller component if it identifies any of them.[1]"}, {"score": 1, "techniqueID": "T1071", "comment": "JPIN can communicate over FTP and send email over SMTP.[1]"}, {"score": 1, "techniqueID": "T1082", "comment": "JPIN can obtain system information such as OS version and disk space.[1]"}, {"score": 1, "techniqueID": "T1016", "comment": "JPIN can obtain network information, including DNS, IP, and proxies.[1]"}, {"score": 1, "techniqueID": "T1033", "comment": "JPIN can obtain the victim user name.[1]"}, {"score": 1, "techniqueID": "T1007", "comment": "JPIN can list running services.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by JPIN", "color": "#66b1ff"}]}