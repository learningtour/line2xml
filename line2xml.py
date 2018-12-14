import subprocess

def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

regel = input("Plak de regel (komma gescheiden): ")

print("Deze gegevens zijn op het klembord geplaatst:")
print("")

data = ""

regelGesplitst = regel.split(",")

for x in regelGesplitst:
	
	if x.strip() != "":
		data = data + ("<activiteit>\n")
		data = data + ("    <code>" + str(x.strip()) + "</code>\n" )
		data = data + ("</activiteit>\n")
		data = data + ("\n")
	
print(data)	
	
write_to_clipboard(data)
