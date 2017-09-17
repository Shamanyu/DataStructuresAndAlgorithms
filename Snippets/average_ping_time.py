import subprocess

totalIpPingTime = 0
averageIpPingTime = 0
totalNamePingTime = 0
averageNamePingTime = 0
counter = 1

while 1:
    pingIpCommand = "ping 8.8.8.8"
    pipeIp = subprocess.Popen(pingIpCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, errors = pipeIp.communicate()
    print ("Output is", output)
    totalIpPingTime += (output.split('')[6]).split('=')[1]
    averageIpPingTime = totalIpPingTime/counter
    pingNameCommand = "ping www.google.com"
    pipeName = subprocess.Popen(directory_management_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, errors = pipeName.communicate()
    totalNamePingTime += (output.split('')[6]).split('=')[1]
    print ("Average www.google.com ping time is ",  totalNamePingTime)
    averageNamePingTime = totalNamePingTime/counter
    counter += 1

