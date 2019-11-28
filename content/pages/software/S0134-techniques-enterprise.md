Title: enterprise Techniques
Template: general/json
save_as: software/S0134/S0134-enterprise-layer.json
json: {"description": "Enterprise techniques used by Downdelph, ATT&CK software S0134 v1.1", "name": "Downdelph (S0134)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1088", "comment": "Downdelph bypasses UAC to escalate privileges by using a custom \"RedirectEXE\" shim database.[1]"}, {"score": 1, "techniqueID": "T1001", "comment": "Downdelph inserts pseudo-random characters between each original character during encoding of C2 network requests, making it difficult to write signatures on them.[1]"}, {"score": 1, "techniqueID": "T1038", "comment": "Downdelph uses search order hijacking of the Windows executable sysprep.exe to escalate privileges.[1]"}, {"score": 1, "techniqueID": "T1105", "comment": "After downloading its main config file, Downdelph downloads multiple payloads from C2 servers.[1]"}, {"score": 1, "techniqueID": "T1032", "comment": "Downdelph uses RC4 to encrypt C2 responses.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Downdelph", "color": "#66b1ff"}]}