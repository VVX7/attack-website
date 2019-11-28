Title: enterprise Techniques
Template: general/json
save_as: software/S0348/S0348-enterprise-layer.json
json: {"description": "Enterprise techniques used by Cardinal RAT, ATT&CK software S0348 v1.0", "name": "Cardinal RAT (S0348)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1059", "comment": "Cardinal RAT can execute commands.[1]"}, {"score": 1, "techniqueID": "T1043", "comment": "Cardinal RAT is downloaded using HTTP over port 443.[1]"}, {"score": 1, "techniqueID": "T1500", "comment": "Cardinal RAT and its watchdog component are compiled and executed after being delivered to victims as embedded, uncompiled source code.[1]"}, {"score": 1, "techniqueID": "T1090", "comment": "Cardinal RAT can act as a reverse proxy.[1]"}, {"score": 1, "techniqueID": "T1024", "comment": "Cardinal RAT uses a secret key with a series of XOR and addition operations to encrypt C2 traffic.[1]"}, {"score": 1, "techniqueID": "T1002", "comment": "Cardinal RAT applies compression to C2 traffic using the ZLIB library.[1]"}, {"score": 1, "techniqueID": "T1140", "comment": "Cardinal RAT decodes many of its artifacts and is decrypted (AES-128) after being downloaded.[1]"}, {"score": 1, "techniqueID": "T1008", "comment": "Cardinal RAT can communicate over multiple C2 host and port combinations.[1]"}, {"score": 1, "techniqueID": "T1083", "comment": "Cardinal RAT checks its current working directory upon execution and also contains watchdog functionality that ensures its executable is located in the correct path (else it will rewrite the payload).[1]"}, {"score": 1, "techniqueID": "T1107", "comment": "Cardinal RAT can uninstall itself, including deleting its executable.[1]"}, {"score": 1, "techniqueID": "T1056", "comment": "Cardinal RAT can log keystrokes.[1]"}, {"score": 1, "techniqueID": "T1112", "comment": "Cardinal RAT sets HKCU\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Windows\\Load to point to its executable.[1]"}, {"score": 1, "techniqueID": "T1027", "comment": "Cardinal RAT encodes many of its artifacts and is encrypted (AES-128) when downloaded. [1]"}, {"score": 1, "techniqueID": "T1057", "comment": "Cardinal RAT contains watchdog functionality that ensures its process is always running, else spawns a new instance.[1]"}, {"score": 1, "techniqueID": "T1055", "comment": "Cardinal RAT injects into a newly spawned process created from a native Windows executable.[1]"}, {"score": 1, "techniqueID": "T1012", "comment": "Cardinal RAT contains watchdog functionality that periodically ensures HKCU\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Windows\\Load is set to point to its executable.[1]"}, {"score": 1, "techniqueID": "T1060", "comment": "Cardinal RAT establishes Persistence by setting the  HKCU\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Windows\\Load Registry key to point to its executable.[1]"}, {"score": 1, "techniqueID": "T1105", "comment": "Cardinal RAT is downloaded and installed via an executed Assess leadership areas of interest payload. Cardinal RAT can also download and execute additional payloads.[1]"}, {"score": 1, "techniqueID": "T1113", "comment": "Cardinal RAT can capture screenshots.[1]"}, {"score": 1, "techniqueID": "T1071", "comment": "Cardinal RAT is downloaded using HTTP over port 443.[1]"}, {"score": 1, "techniqueID": "T1082", "comment": "Cardinal RAT can collect the hostname, Microsoft Windows version, and processor architecture from a victim machine.[1]"}, {"score": 1, "techniqueID": "T1033", "comment": "Cardinal RAT can collect the username from a victim machine.[1]"}, {"score": 1, "techniqueID": "T1204", "comment": "Cardinal RAT lures victims into executing malicious macros embedded within Microsoft Excel documents.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Cardinal RAT", "color": "#66b1ff"}]}