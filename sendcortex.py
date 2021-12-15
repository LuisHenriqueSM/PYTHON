import socket

    edsIP: str = "10.163.155.106"
    edsPORT = 3003
    MESSAGE=b'499602d2000000280000000000000001000000010000000000000000b669fd2e'

    srvsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srvsock.settimeout(3) # 3 second timeout on commands
    srvsock.connect((edsIP, edsPORT)))
    srvsock.sendall(MESSAGE)



    srvsock.close()