Title: enterprise Techniques
Template: general/json
save_as: software/S0410/S0410-enterprise-layer.json
json: {"description": "Enterprise techniques used by Fysbis, ATT&CK software S0410 v1.0", "name": "Fysbis (S0410)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1059", "comment": "Fysbis has the ability to create and execute commands in a remote shell for CLI.[1]"}, {"score": 1, "techniqueID": "T1043", "comment": "Fysbis has used port 80 for C2. [1]"}, {"score": 1, "techniqueID": "T1132", "comment": "Fysbis can use Base64 to encode its C2 traffic.[2]"}, {"score": 1, "techniqueID": "T1083", "comment": "Fysbis has the ability to search for files. [2]"}, {"score": 1, "techniqueID": "T1107", "comment": "Fysbis has the ability to delete files.[2]"}, {"score": 1, "techniqueID": "T1056", "comment": "Fysbis can perform keylogging. [1]"}, {"score": 1, "techniqueID": "T1036", "comment": "Fysbis has masqueraded as trusted software rsyncd and dbus-inotifier.[2]"}, {"score": 1, "techniqueID": "T1027", "comment": "Fysbis has been encrypted using XOR and RC4. [2]"}, {"score": 1, "techniqueID": "T1057", "comment": "Fysbis can collect information about running processes. [2]"}, {"score": 1, "techniqueID": "T1082", "comment": "Fysbis has used the command ls /etc | egrep -e\"fedora*|debian*|gentoo*|mandriva*|mandrake*|meego*|redhat*|lsb-*|sun-*|SUSE*|release\" to determine which Linux OS version is running.[1]"}, {"score": 1, "techniqueID": "T1501", "comment": "Fysbis has established persistence using a systemd service. [2]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by Fysbis", "color": "#66b1ff"}]}