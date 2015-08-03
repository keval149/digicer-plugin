"""
.. module: lemur.plugins.lemur_verisign.verisign
    :platform: Unix
    :synopsis: This module is responsible for communicating with the VeriSign VICE 2.0 API.
    :copyright: (c) 2015 by Netflix Inc., see AUTHORS for more
    :license: Apache, see LICENSE for more details.

.. moduleauthor:: Kevin Glisson <kglisson@netflix.com>
"""
import arrow
import requests
import xmltodict

from flask import current_app

from lemur.plugins.bases import IssuerPlugin
from lemur.plugins import lemur_digicert as digicert
from lemur.plugins import lemur_digicert as verisign
from lemur.plugins.lemur_digicert import constants
from lemur.plugins.lemur_verisign import constants
from lemur.common.utils import get_psuedo_random_string

print "New module fro digicert"
# https://support.venafi.com/entries/66445046-Info-VeriSign-Error-Codes


print "DigicertIssuerPlugin"
class DigicertIssuerPlugin(IssuerPlugin):
    title = 'Digicert'
    slug = 'digicert-issuer'
    description = 'Enables the creation of certificates by the digicert test API.'
    version = digicert.VERSION

    author = 'Keval Doshi'
    author_url = 'https://github.com/netflix/lemur'

    def __init__(self, *args, **kwargs):
        return "<p>Absolutely useless widget</p>"

    def create_certificate(self, csr, issuer_options):
        """
        Creates a Verisign certificate.

        :param csr:
        :param issuer_options:
        :return: :raise Exception:
        """
	"""
        url = current_app.config.get("VERISIGN_URL") + '/enroll'

        data = process_options(issuer_options)
        data['csr'] = csr

        current_app.logger.info("Requesting a new verisign certificate: {0}".format(data))

        response = self.session.post(url, data=data)
        cert = handle_response(response.content)['Response']['Certificate']
        return cert, constants.VERISIGN_INTERMEDIATE,
	"""
	print "I am in Create_certificate"
    @staticmethod
    def create_authority(options):
        """
        Creates an authority, this authority is then used by Lemur to allow a user
        to specify which Certificate Authority they want to sign their certificate.

        :param options:
        :return:
        """
	"""        
	role = {'username': '', 'password': '', 'name': 'verisign'}
        return constants.VERISIGN_ROOT, "", [role]
	"""
	print "I am in create authority"
