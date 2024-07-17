# The socket API is an application-level network protocol,
# via file transfer protocol (FTP) and hyper transfer protocol
from socket import *
# The import of time is useful to define how much time has passed
import time


#this function takes note of what time it is currently, this is useful later
startTime = time.time()
#this runs the if statement if the name is the same as the main function or the universal
#function, then the if statement will run
if __name__ == '__main__':
    #this asks who needs to be asked
    target = input('Enter the host to be scanned: ')
    #this function takes the input given and uses
    #gethostbyname
    t_IP = gethostbyname(target)
    print('Starting scan on host: ', t_IP)

#this function specifies the ports within the range of 50,500
    #after this, the function s is created, and inside, is the use
    #of the socket apt and the use of AF_INET and SockStream
    #which specifies designates the address and then finds TCP sockets,
    #the use of SOCK_DGRAM instead of SOCK_STREAM would find UDP sockets
    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)
#this function, conn, uses s, which is address designation,
        #and TCP sockets, which are then used by connect_ex
        #which connects to the address, and then is specific
        #by the function t_ip which is the input, and then i,
        #the range of ports to search. if that connection equals 0,
        #then it will return that the port is open. then the function closes
        conn = s.connect_ex((t_IP, i))
        if conn == 0:
            print('Port %d: OPEN' % (i,))
        s.close()
        #this final print statement is important because it prints how much
        #time it has taken to complete this scan by taking the original
        #function used at the top, startime, and subtracts it by the current time.
print('Time taken:', time.time() - startTime)
