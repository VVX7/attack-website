Title: enterprise Techniques
Template: general/json
save_as: software/S0282/S0282-enterprise-layer.json
json: {"description": "Enterprise techniques used by MacSpy, ATT&CK software S0282 v1.0", "name": "MacSpy (S0282)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1123", "comment": "MacSpy can record the sounds from microphones on a computer.[1]"}, {"score": 1, "techniqueID": "T1115", "comment": "MacSpy can steal clipboard contents.[1]"}, {"score": 1, "techniqueID": "T1107", "comment": "MacSpy deletes any temporary files it creates[2]"}, {"score": 1, "techniqueID": "T1158", "comment": "MacSpy stores itself in ~/Library/.DS_Stores/[2]"}, {"score": 1, "techniqueID": "T1056", "comment": "MacSpy captures keystrokes.[1]"}, {"score": 1, "techniqueID": "T1159", "comment": "MacSpy persists via a Launch Agent.[1]"}, {"score": 1, "techniqueID": "T1188", "comment": "MacSpy uses Tor for command and control.[1]"}, {"score": 1, "techniqueID": "T1113", "comment": "MacSpy can capture screenshots of the desktop over multiple monitors.[1]"}, {"score": 1, "techniqueID": "T1071", "comment": "MacSpy uses HTTP for command and control.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by MacSpy", "color": "#66b1ff"}]}