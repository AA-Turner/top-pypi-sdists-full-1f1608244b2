import logging
import asyncio

from minikerberos import logger
from minikerberos.common.factory import KerberosClientFactory, kerberos_url_help_epilog
from minikerberos.common.constants import KerberosSecretType
from minikerberos.common.spn import KerberosSPN
from minikerberos.common.creds import KerberosCredential
from minikerberos.common.kirbi import Kirbi

async def dMSA(kerberos_url, targetuser, kirbifile = None, ccachefile = None):
	cu = KerberosClientFactory.from_url(kerberos_url)
	client = cu.get_client()
	target_user = KerberosSPN.from_upn(targetuser)
	
	if cu.secret_type != KerberosSecretType.CCACHE:
		logger.debug('Getting TGT')
		await client.get_TGT()
		logger.debug('Getting DMSA')
		tgs, encTGSRepPart, key = await client.dmsa(target_user)
	else:
		logger.debug('Getting TGS via TGT from CCACHE')
		for kirbi in client.credential.ccache.get_all_tgt_kirbis():
			try:
				logger.info('Trying to get SPN with %s' % kirbi.get_username())
				ccred_test = KerberosCredential.from_kirbi(kirbi.to_hex(), encoding='hex')
				client = cu.get_client_newcred(ccred_test)
				tgs, encTGSRepPart, key = await client.dmsa(target_user)
				logger.info('Sucsess!')
				break
			except Exception as e:

				logger.debug('This ticket is not usable it seems Reason: %s' % e)
				continue
	
	if ccachefile is not None:
		client.ccache.to_file(ccachefile)
		print('Ticket stored in ccache file %s' % ccachefile)
	
	kirbi = Kirbi.from_ticketdata(tgs, encTGSRepPart)
	print(str(kirbi))
	if kirbifile is not None:
		kirbi.to_file(kirbifile)
	logging.info('Done!')


def main():
	import argparse
	
	parser = argparse.ArgumentParser(description='Gets an S4U2self ticket impersonating given user', formatter_class=argparse.RawDescriptionHelpFormatter, epilog = kerberos_url_help_epilog)
	parser.add_argument('--kirbi', help='kirbi file to store the TGS ticket in, otherwise kirbi will be printed to stdout')
	parser.add_argument('--ccache', help='ccache file to store the TGT ticket in')
	parser.add_argument('-v', '--verbose', action='count', default=0)
	parser.add_argument('kerberos_url', help='Machine account credentials in kerberos URL format.')
	parser.add_argument('targetuser', help='')
	
	args = parser.parse_args()
	if args.verbose == 0:
		logger.setLevel(logging.WARNING)
	elif args.verbose == 1:
		logger.setLevel(logging.INFO)
	else:
		logger.setLevel(1)

	asyncio.run(dMSA(args.kerberos_url, args.targetuser, args.kirbi, args.ccache))
	
	
if __name__ == '__main__':
	main()