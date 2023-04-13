
# - Try to calculate the distance between the letter 'M' and 'C' and find a way to get another letter using the value you get each time 

with open(r'C:\Users\zerou\Documents\PythonWS\MC-decode-challenge\message.txt' , 'r') as Msg:
    msg = Msg.readline()
    d_msg = ''
    while msg:
        d_msg += chr(msg.index('C') - msg.index('M') - 1)
        msg = msg[msg.index('C')+1::]

    print(d_msg)