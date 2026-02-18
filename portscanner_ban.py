import socket
def bannerGrabber(inputIp,inputPort):
    try:
        s = socket.socket()
        s.connect((inputIp,inputPort))
        s.settimeout(5)
        bannerData = s.recv(1024).decode()
        if bannerData:
            print(f"Banner details: {bannerData}")
        else:
            print("Could not connect to the service.")
       
    except socket.timeout:
        print("Request timeout")
    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        s.close()

def main():
    inputIp = str(input("Enter the target ip address: "))
    inputPort =  int(input("Enter the port: "))
   
    bannerGrabber(inputIp,inputPort)
   
 
if __name__=="__main__":
    main()