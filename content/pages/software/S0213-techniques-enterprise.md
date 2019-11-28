Title: enterprise Techniques
Template: general/json
save_as: software/S0213/S0213-enterprise-layer.json
json: {"description": "Enterprise techniques used by DOGCALL, ATT&CK software S0213 v1.1", "name": "DOGCALL (S0213)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1123", "comment": "DOGCALL can capture microphone data from the victim's machine.[2]"}, {"score": 1, "techniqueID": "T1056", "comment": "DOGCALL is capable of logging keystrokes.[1][2]"}, {"score": 1, "techniqueID": "T1027", "comment": "DOGCALL is encrypted using single-byte XOR.[2]"}, {"score": 1, "techniqueID": "T1105", "comment": "DOGCALL can download and execute additional payloads.[2]"}, {"score": 1, "techniqueID": "T1113", "comment": "DOGCALL is capable of capturing screenshots of the victim's machine.[1][2]"}, {"score": 1, "techniqueID": "T1102", "comment": "DOGCALL is capable of leveraging cloud storage APIs such as Cloud, Box, Dropbox, and Yandex for C2.[1][2]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by DOGCALL", "color": "#66b1ff"}]}