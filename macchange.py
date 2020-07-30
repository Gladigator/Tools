import subprocess

interface = input("Enter Interface: ")
mac = input("Enter Mac Address: ")

#print("Changing the Mac Address " + interface + " to " + mac)

#subprocess.call("ifconfig", shell=True)
#subprocess.call("ifconfig " + interface + " down", shell=True)
#subprocess.call("ifconfig " + interface + " hw ether " + mac, shell=True)
#subprocess.call("ifconfig " + interface + " up", shell=True)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac])
subprocess.call(["ifconfig", interface, "up"])


subprocess.call("ifconfig", shell=True)
print("---------------------")
print("---------------------")
print("---------------------")
print("Mac Address Changed Sucessfully")






















