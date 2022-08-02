from utils.dbconfig import dbconfig
import utils.aesutil
from getpass import getpass
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
import base64
from rich import print as printc
from rich.console import Console

def computeMasterKey(mp,ds):
	password = mp.encode()
	salt = ds.encode()
	key = PBKDF2(password, salt, 32, count=1000000, hmac_hash_module=SHA512)
	return key


def checkEntryForDelete(sitename):
	db = dbconfig()
	cursor = db.cursor()
	query = f"SELECT * FROM pmdatabase.entries WHERE sitename = '{sitename}'"
	cursor.execute(query)
	results = cursor.fetchall()

	if len(results)!=0:
		return False
	return True


def deleteEntry(sitename, siteurl, email, username):
    # check entry existence
	if checkEntryForDelete(sitename):
		printc("[yellow][-] There aren't any entries with those parameters...[/yellow]")
		return

	# remove from database	
	db = dbconfig()
	cursor = db.cursor()
	query = "DELETE FROM pmdatabase.entries WHERE sitename = %s AND siteurl = %s AND email = %s AND username = %s LIMIT 1"
	tuple1 = (sitename,siteurl,email,username)
	cursor.execute(query, tuple1)
	db.commit()

	printc("[red][-][/red] Entry Deleted ")
