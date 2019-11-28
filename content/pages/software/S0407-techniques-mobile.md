Title: mobile Techniques
Template: general/json
save_as: software/S0407/S0407-mobile-layer.json
json: {"description": "Mobile techniques used by Monokle, ATT&CK software S0407 v1.0", "name": "Monokle (S0407)", "domain": "mitre-mobile", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1435", "comment": "Monokle can retrieve calendar event information including the event name, when and where it is taking place, and the description. [1]"}, {"score": 1, "techniqueID": "T1433", "comment": "Monokle can retrieve call history.[1]"}, {"score": 1, "techniqueID": "T1432", "comment": "Monokle can retrieve the device's contact list.[1]"}, {"score": 1, "techniqueID": "T1438", "comment": "Monokle can be controlled via email and SMS/phone call from a set of \"control phones.\"[1]"}, {"score": 1, "techniqueID": "T1418", "comment": "Monokle can list applications installed on the device.[1]"}, {"score": 1, "techniqueID": "T1429", "comment": "Monokle can record audio from the device's microphone and can record phone calls, specifying the output audio quality.[1]"}, {"score": 1, "techniqueID": "T1512", "comment": "Monokle can take photos and videos.[1]"}, {"score": 1, "techniqueID": "T1533", "comment": "Monokle can retrieve the salt used when storing the user\u2019s password, aiding an adversary in computing the user\u2019s plaintext password/PIN from the stored password hash. Monokle can also capture the user\u2019s dictionary, user-defined shortcuts, and browser history, enabling profiling of the user and their activities.[1]"}, {"score": 1, "techniqueID": "T1447", "comment": "Monokle can delete arbitrary files on the device, and can also uninstall itself and clean up staging files.[1]"}, {"score": 1, "techniqueID": "T1446", "comment": "Monokle can reset the user's password/PIN.[1]"}, {"score": 1, "techniqueID": "T1417", "comment": "Monokle can record the user's keystrokes.[1]"}, {"score": 1, "techniqueID": "T1430", "comment": "Monokle can track the device's location.[1]"}, {"score": 1, "techniqueID": "T1400", "comment": "Monokle can remount the system partition as read/write to install attacker-specified certificates. [1]"}, {"score": 1, "techniqueID": "T1507", "comment": "Monokle can retrieve nearby cell tower and Wi-Fi network information.[1]"}, {"score": 1, "techniqueID": "T1410", "comment": "Monokle can install attacker-specified certificates to the device's trusted certificate store, enabling an adversary to perform man-in-the-middle attacks. [1]"}, {"score": 1, "techniqueID": "T1406", "comment": "Monokle uses XOR to obfuscate its second stage binary.[1]"}, {"score": 1, "techniqueID": "T1513", "comment": "Monokle can record the screen as the user unlocks the device and can take screenshots of any application in the foreground. Monokle can also abuse accessibility features to read the screen to capture data from a large number of popular applications.[1]"}, {"score": 1, "techniqueID": "T1426", "comment": "Monokle queries the device for metadata such as make, model, and power levels.[1]"}, {"score": 1, "techniqueID": "T1422", "comment": "Monokle checks if the device is connected via Wi-Fi or mobile data.[1]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Monokle", "color": "#66b1ff"}]}