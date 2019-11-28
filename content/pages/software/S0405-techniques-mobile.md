Title: mobile Techniques
Template: general/json
save_as: software/S0405/S0405-mobile-layer.json
json: {"description": "Mobile techniques used by Exodus, ATT&CK software S0405 v1.0", "name": "Exodus (S0405)", "domain": "mitre-mobile", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1435", "comment": "Exodus Two can exfiltrate calendar events. [1]"}, {"score": 1, "techniqueID": "T1433", "comment": "Exodus Two can exfiltrate the call log. [1]"}, {"score": 1, "techniqueID": "T1432", "comment": "Exodus Two can download the address book. [1]"}, {"score": 1, "techniqueID": "T1409", "comment": "Exodus Two extracts information from Facebook, Facebook Messenger, Gmail, IMO, Skype, Telegram, Viber, WhatsApp, and WeChat.[1]"}, {"score": 1, "techniqueID": "T1418", "comment": "Exodus Two can obtain a list of installed applications. [1]"}, {"score": 1, "techniqueID": "T1429", "comment": "Exodus Two can record audio from the compromised device's microphone and can record call audio in 3GP format. [1]"}, {"score": 1, "techniqueID": "T1512", "comment": "Exodus Two can take pictures with the device cameras. [1]"}, {"score": 1, "techniqueID": "T1412", "comment": "Exodus Two can capture SMS messages.[1]"}, {"score": 1, "techniqueID": "T1532", "comment": "Exodus One encrypts data using XOR prior to exfiltration. [1]"}, {"score": 1, "techniqueID": "T1533", "comment": "Exodus Two can extract information on pictures from the Gallery, Chrome and SBrowser bookmarks, and the connected WiFi network's password.[1]"}, {"score": 1, "techniqueID": "T1475", "comment": "Exodus One has been distributed via the Play Store. [1]"}, {"score": 1, "techniqueID": "T1407", "comment": "Exodus One, after checking in, sends a POST request and then downloads  Exodus Two, the second stage binaries. [1]"}, {"score": 1, "techniqueID": "T1404", "comment": "Exodus Two attempts to elevate privileges by using a modified version of the DirtyCow exploit. [1]"}, {"score": 1, "techniqueID": "T1430", "comment": "Exodus Two can extract the GPS coordinates of the device.[1]"}, {"score": 1, "techniqueID": "T1507", "comment": "Exodus Two collects a list of nearby base stations. [1]"}, {"score": 1, "techniqueID": "T1513", "comment": "Exodus Two can take screenshots of any application in the foreground. [1]"}, {"score": 1, "techniqueID": "T1437", "comment": "Exodus One checks in with the command and control server using HTTP POST requests. [1]"}, {"score": 1, "techniqueID": "T1422", "comment": "Exodus One queries the device for its IMEI code and the phone number in order to validate the target of a new infection. [1]"}, {"score": 1, "techniqueID": "T1509", "comment": "Exodus Two attempts to connect to port 22011 to provide a remote reverse shell.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Exodus", "color": "#66b1ff"}]}