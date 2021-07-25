import socket
import sys
import time


class Scanner:
    
    def __init__(self):
        print('''
  _____           _      _____                                 
 |  __ \         | |    / ____|                                
 | |__) |__  _ __| |_  | (___   ___ __ _ _ __  _ __   ___ _ __ 
 |  ___/ _ \| '__| __|  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 | |  | (_) | |  | |_   ____) | (_| (_| | | | | | | |  __/ |   
 |_|   \___/|_|   \__| |_____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                               
        ''')
        
        self.scanner=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print('Started the Scanner Enter the Option Number to Scan or press Ctrl-C to quit')
        self.host='192.168.0.105'

        self.common_ports={20:"File Transfer Protocol (FTP) Data Transfer",21:"File Transfer Protocol (FTP) Command Control",
        22:"Secure Shell (SSH)",23:"Telnet - Remote login service, unencrypted text messages",
        25:"Simple Mail Transfer Protocol (SMTP) E-mail Routing",53:"Domain Name System (DNS) service",
        80:"Hypertext Transfer Protocol (HTTP) used in World Wide Web",
        110:"Post Office Protocol (POP3) used by e-mail clients to retrieve e-mail from a server",
        119:"Network News Transfer Protocol (NNTP)",
        123:"Network Time Protocol (NTP)",143:"Internet Message Access Protocol (IMAP) Management of Digital Mail",
        161:"Simple Network Management Protocol (SNMP)",194:"Internet Relay Chat (IRC)",
        443:"HTTP Secure (HTTPS) HTTP over TLS/SSL"}

    
    def scan_common_ports(self):
        '''Scanning common ports'''

        start_time=time.perf_counter()
        print('\n\tScanning Common Ports\t')
        print('---'*15)
        
        for port,info in self.common_ports.items():
            try:
                print('Scanning Port {} : {}'.format(port,info))
                self.scanner.connect((self.host,port))
                print('Port {} :\tOpen'.format(port))
                self.stop_scanner()

            except Exception:
                print('Port {} :\tClosed'.format(port))
        end_time=time.perf_counter()
        print('Time taken to scan common ports is: {:.2f} second(s)'.format(end_time-start_time))

    
    
    def scan_port(self):
        '''Scanning the Ports that are specified'''

        start_time=time.perf_counter()
        print('\n\tScanning Custom Ports\t')
        print('---'*15)

        print('\nNote:\n Please input all the ports you want to scan with a comma in between them.\n\n')
        ports=input('Enter All the port Numbers you want to scan: ')

        for port in ports.split(','):
            try:
                print('Scanning Port {}'.format(port))
                self.scanner.connect((self.host,port))
                print('Port {} :\tOpen'.format(port))
                self.stop_scanner()

            except Exception:
                print('Port {} :\tClosed'.format(port))
        
        end_time=time.perf_counter()
        print('Time taken to scan {} is: {:.2f} second(s)'.format(ports,end_time-start_time))

    
    
    def scan_all_ports(self):
        '''Scanning All the Ports'''

        start_time=time.perf_counter()
        print('\n\tScanning All Ports\t')
        print('---'*15)

        for port in range(20,130000):
            try:
                print('Scanning Port {}'.format(port))
                self.scanner.connect((self.host,port))
                print('Port {} :\tOpen'.format(port))
                self.stop_scanner()

            except Exception:
                print('Port {} :\tClosed'.format(port))
        end_time=time.perf_counter()
        print('Time taken to scan all ports is: {:.2f} second(s)'.format(end_time-start_time))


    def stop_scanner(self):
        '''Closes the Scanner'''

        self.scanner.close()




if __name__=="__main__":

    scanner=Scanner()

    try:

        for option in ['1.Scan All Ports','2.Scan Common Ports','3.Scan Custom Port']:
            print(option)

        opt=int(input('Enter Option Number: '))


        print('Do you want to do Multiple Scans:')

        for option in ['1.Yes','2.No']:
            print(option)

        multiscan=int(input('Enter Option Number:'))

        if opt==1:
            if multiscan==1:
                while True:
                    try:
                        scanner.scan_all_ports()
                        time.sleep(10)

                    except KeyboardInterrupt:
                        print('Stopping Multi Scan as you pressed Ctrl-C')
                        break

            else:
                scanner.scan_all_ports()


        elif opt==2:
            if multiscan==1:
                while True:
                    try:
                        scanner.scan_common_ports()
                        time.sleep(10)

                    except KeyboardInterrupt:
                        print('Stopping Multi Scan as you pressed Ctrl-C')
                        break

            else:
                scanner.scan_common_ports()


        elif opt==3:
            if multiscan==1:
                while True:
                    try:
                        scanner.scan_port()
                        time.sleep(10)

                    except KeyboardInterrupt:
                        print('Stopping Multi Scan as you pressed Ctrl-C')
                        break
            else:
                scanner.scan_port()

        else:
            print('Wrong Option Try Again')
    
    except KeyboardInterrupt:
        print('Exiting Port Scanner')
        scanner.stop_scanner()
        sys.exit(0)
