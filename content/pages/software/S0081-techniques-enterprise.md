Title: enterprise Techniques
Template: general/json
save_as: software/S0081/S0081-enterprise-layer.json
json: {"description": "Enterprise techniques used by Elise, ATT&CK software S0081 v1.1", "name": "Elise (S0081)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1087", "comment": "Elise executes net user after initial communication is made to the remote server.[1]"}, {"score": 1, "techniqueID": "T1132", "comment": "Elise exfiltrates data using cookie values that are Base64-encoded.[1]"}, {"score": 1, "techniqueID": "T1074", "comment": "Elise creates a file in AppData\\Local\\Microsoft\\Windows\\Explorer and stores all harvested data in that file.[2]"}, {"score": 1, "techniqueID": "T1083", "comment": "A variant of Elise executes dir C:\\progra~1 when initially run."}, {"score": 1, "techniqueID": "T1107", "comment": "Elise is capable of launching a remote shell on the host to delete itself.[2]"}, {"score": 1, "techniqueID": "T1036", "comment": "If installing itself as a service fails, Elise instead writes itself as a file named svchost.exe saved in %APPDATA%\\Microsoft\\Network.[1]"}, {"score": 1, "techniqueID": "T1050", "comment": "Elise configures itself as a service.[1]"}, {"score": 1, "techniqueID": "T1027", "comment": "Elise encrypts several of its files, including configuration files.[1]"}, {"score": 1, "techniqueID": "T1057", "comment": "Elise enumerates processes via the tasklist command.[2]"}, {"score": 1, "techniqueID": "T1055", "comment": "Elise injects DLL files into iexplore.exe.[1][2]"}, {"score": 1, "techniqueID": "T1060", "comment": "If establishing persistence by installation as a new service fails, one variant of Elise establishes persistence for the created .exe file by setting the following Registry key: HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\svchost : %APPDATA%\\Microsoft\\Network\\svchost.exe. Other variants have set the following Registry keys for persistence: HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\imejp : [self] and HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\IAStorD.[1][2]"}, {"score": 1, "techniqueID": "T1105", "comment": "Elise can download additional files from the C2 server for execution.[2]"}, {"score": 1, "techniqueID": "T1085", "comment": "After copying itself to a DLL file, a variant of Elise calls the DLL file using rundll32.exe.[1]"}, {"score": 1, "techniqueID": "T1071", "comment": "Elise communicates over HTTP or HTTPS for C2.[1]"}, {"score": 1, "techniqueID": "T1032", "comment": "Elise encrypts exfiltrated data with RC4.[1]"}, {"score": 1, "techniqueID": "T1082", "comment": "Elise executes systeminfo after initial communication is made to the remote server.[1]"}, {"score": 1, "techniqueID": "T1016", "comment": "Elise executes ipconfig /all after initial communication is made to the remote server.[1][2]"}, {"score": 1, "techniqueID": "T1007", "comment": "Elise executes net start after initial communication is made to the remote server.[1]"}, {"score": 1, "techniqueID": "T1099", "comment": "Elise performs timestomping of a CAB file it creates.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Elise", "color": "#66b1ff"}]}