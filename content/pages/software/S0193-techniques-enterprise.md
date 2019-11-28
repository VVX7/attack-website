Title: enterprise Techniques
Template: general/json
save_as: software/S0193/S0193-enterprise-layer.json
json: {"description": "Enterprise techniques used by Forfiles, ATT&CK software S0193 v1.0", "name": "Forfiles (S0193)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1005", "comment": "Forfiles can be used to act on (ex: copy, move, etc.) files/directories in a system during (ex: copy files into a staging area before).[4]"}, {"score": 1, "techniqueID": "T1083", "comment": "Forfiles can be used to locate certain types of files/directories in a system.(ex: locate all files with a specific extension, name, and/or age)[4]"}, {"score": 1, "techniqueID": "T1202", "comment": "Forfiles can be used to subvert controls and possibly conceal command execution by not directly invoking cmd.[2][3]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Forfiles", "color": "#66b1ff"}]}