from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n Test SMTP"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver,port)

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    mail =('MAIL FROM: <pkm5782@nyu.edu>')
    clientSocket.send(mail.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2)
    if recv2[:3] != '250': #if the data is not received
     print('250 reply not received from server.!')

   # Send RCPT TO command and handle server response.
    rcpt = ('RCPT TO: <priyankamarwal@gmail.com>')
    clientSocket.send(rcpt.encode())
    recv3 = clientSocket.recv(1024).decode()
   #print(recv3)
    if recv3[:3] != '250':  # if the data is not received
     print('250 reply not received from server.')

   # Send DATA command and handle server response.
    data = "DATA \r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print(recv4)
    if recv4[:3] != '354':  # if the data is not received
     print('354 reply not received from server.')

   # Send message data.
    subject = "Subject: testing my client\r\n\r\n"
    clientSocket.send(subject.encode())
    clientSocket.send(msg.encode())
    clientSocket.send(endmsg.encode())

   # Message ends with a single period, send message end and handle server response.
    recv_msg = clientSocket.recv(1024)
   #print("Response after sending message body:" + recv_msg.decode())

   # Send QUIT command and handle server response.
    quitcommand = ('QUIT\r\n')
    clientSocket.send(quitcommand.encode())
    recv5 = clientSocket.recv(1024).decode()
   #print(recv5)

    clientSocket.close()

    if __name__ == '__main__':
     smtp_client(1025, '127.0.0.1')