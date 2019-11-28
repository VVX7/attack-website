Title: enterprise Techniques
Template: general/json
save_as: software/S0412/S0412-enterprise-layer.json
json: {"description": "Enterprise techniques used by ZxShell, ATT&CK software S0412 v1.0", "name": "ZxShell (S0412)", "domain": "mitre-enterprise", "version": "2.2", "techniques": [{"score": 1, "techniqueID": "T1134", "comment": "ZxShell has a command called RunAs, which creates a new process as another user or process context. [2]"}, {"score": 1, "techniqueID": "T1059", "comment": "ZxShell can launch a reverse command shell.[1][2][3]"}, {"score": 1, "techniqueID": "T1043", "comment": "ZxShell uses common ports such as 80 and 443 for C2.[2]"}, {"score": 1, "techniqueID": "T1090", "comment": "ZxShell can set up an HTTP or SOCKS proxy. [1][2]"}, {"score": 1, "techniqueID": "T1136", "comment": "ZxShell has a feature to create local user accounts.[2]"}, {"score": 1, "techniqueID": "T1089", "comment": "ZxShell can disable the firewall by modifying the registry key HKLM\\SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\StandardProfile and killing AV products' processes. [2]"}, {"score": 1, "techniqueID": "T1499", "comment": "ZxShell has a feature to perform SYN flood attack on a host. [1][2]"}, {"score": 1, "techniqueID": "T1083", "comment": "ZxShell has a command to open a file manager and explorer on the system. [2]"}, {"score": 1, "techniqueID": "T1107", "comment": "ZxShell can delete files from the system. [1][2]"}, {"score": 1, "techniqueID": "T1179", "comment": "ZxShell hooks several API functions to spawn system threads. [2]"}, {"score": 1, "techniqueID": "T1070", "comment": "ZxShell has a command to clear system event logs. [2]"}, {"score": 1, "techniqueID": "T1056", "comment": "ZxShell has a feature to capture a remote computer's keystrokes using a keylogger. [1][2]"}, {"score": 1, "techniqueID": "T1046", "comment": "ZxShell can launch port scans. [1][2]"}, {"score": 1, "techniqueID": "T1050", "comment": "ZxShell can create a new service using the service parser function ProcessScCommand. [2]"}, {"score": 1, "techniqueID": "T1057", "comment": "ZxShell has a command, ps, to obtain a listing of processes on the system. [2]"}, {"score": 1, "techniqueID": "T1055", "comment": "ZxShell is injected into a shared SVCHOST process. [2]"}, {"score": 1, "techniqueID": "T1012", "comment": "ZxShell can query the netsvc group value data located in the svchost group Registry key. [2]"}, {"score": 1, "techniqueID": "T1076", "comment": "ZxShell has remote desktop functionality. [2]"}, {"score": 1, "techniqueID": "T1105", "comment": "ZxShell has a command to transfer files from a remote host. [2]"}, {"score": 1, "techniqueID": "T1021", "comment": "ZxShell supports functionality for VNC sessions. [2]"}, {"score": 1, "techniqueID": "T1085", "comment": "ZxShell has used rundll32.exe to execute other DLLs and named pipes. [2]"}, {"score": 1, "techniqueID": "T1113", "comment": "ZxShell can capture screenshots.[1]"}, {"score": 1, "techniqueID": "T1071", "comment": "ZxShell has used HTTP and FTP for connections. [2]"}, {"score": 1, "techniqueID": "T1082", "comment": "ZxShell can collect the local hostname, operating system details, CPU speed, and total physical memory. [2]"}, {"score": 1, "techniqueID": "T1033", "comment": "ZxShell can collect the owner and organization information from the target workstation. [2]"}, {"score": 1, "techniqueID": "T1007", "comment": "ZxShell can check the services on the system. [2]"}, {"score": 1, "techniqueID": "T1065", "comment": "ZxShell uses ports 1985 and 1986 for communication. [2]"}, {"score": 1, "techniqueID": "T1125", "comment": "ZxShell has a command to perform video device spying. [2]"}], "gradient": {"colors": ["#ffffff", "#66b1ff"], "minValue": 0, "maxValue": 1}, "legendItems": [{"label": "used by ZxShell", "color": "#66b1ff"}]}