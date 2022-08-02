import argparse
from getpass import getpass
import hashlib
import pyperclip
from rich import print as printc
import utils.add
import utils.retrieve
import utils.generate
from utils.dbconfig import dbconfig
import utils.delete

# arguments
parser = argparse.ArgumentParser(description='Arguments')
parser.add_argument('option', help='(a)dd / (d)elete / (e)xtract / (g)enerate')
parser.add_argument("-s", "--name", help="Site name")
parser.add_argument("-u", "--url", help="Site URL")
parser.add_argument("-e", "--email", help="Email")
parser.add_argument("-l", "--login", help="Username")
parser.add_argument("--length", help="Length of the password to generate",type=int)
parser.add_argument("-c", "--copy", action='store_true', help='Copy password to clipboard')
args = parser.parse_args()

def inputAndValidateMasterPassword():
	mp = getpass("MASTER PASSWORD: ")
    # hash encrypt mp
	hashed_mp = hashlib.sha256(mp.encode()).hexdigest()
	db = dbconfig()
	cursor = db.cursor()
	query = "SELECT * FROM pmdatabase.secrets"
	cursor.execute(query)
	result = cursor.fetchall()[0]
	if hashed_mp != result[0]:
		printc("[red][!] WRONG! [/red]")
		return None

	return [mp,result[1]]

def main():
	if args.option in ["add","a"]:
		if args.name == None or args.url == None or args.login == None:
			if args.name == None:
				printc("[red][!]Site Name (-s) is required and was not specified[/red] ")
			if args.url == None:
				printc("[red][!] Site URL (-u) is required and was not specified[/red]")
			if args.login == None:
				printc("[red][!] Site Login User or Name (-l) is required and was not specified[/red]")
			return

		if args.email == None:
			args.email = ""

		res = inputAndValidateMasterPassword()
		if res is not None:
			utils.add.addEntry(res[0],res[1],args.name,args.url,args.email,args.login)
   
	if args.option in ["delete","d"]:
		if args.name == None or args.url == None or args.login == None:
			if args.name == None:
				printc("[red][!] Site Name (-s) is required and was not specified[/red]")
			if args.url == None:
				printc("[red][!] Site URL (-u) is required and was not specified[/red]")
			if args.login == None:
				printc("[red][!] Site Login User or Name (-l) is required and was not specified[/red]")
			if args.email == None:
				printc("[red][!] Site Email (-e) is required and was not specified[/red]")
			return
		
		res = inputAndValidateMasterPassword()
		if res is not None:
			utils.delete.deleteEntry(args.name,args.url,args.email,args.login)

	if args.option in ["extract","e"]:
		res = inputAndValidateMasterPassword()
		search = {}
		if args.name is not None:
			search["sitename"] = args.name
		if args.url is not None:
			search["siteurl"] = args.url
		if args.email is not None:
			search["email"] = args.email
		if args.login is not None:
			search["username"] = args.login
		if res is not None:
			utils.retrieve.retrieveEntries(res[0],res[1],search,decryptPassword = args.copy)

	if args.option in ["generate","g"]:
		if args.length == None:
			printc("[red][+][/red] Specify length of the password to generate (--length)")
			return
		password = utils.generate.generatePassword(args.length)
		pyperclip.copy(password)
		printc("[green][+][/green] Password generated and copied to clipboard")

main()