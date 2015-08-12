"""
"""
from flask import current_app

from lemur.plugins.bases import IssuerPlugin
import lemur_digicert as digicert
from lemur_digicert import constants

class DigicertIssuerPlugin(IssuerPlugin):
    title = 'Digicert'
    slug = 'digicert-issuer'
    description = 'Enables the creation of certificates by the digicert test API.'
    version = digicert.VERSION

    author = 'Keval Doshi'
    author_url = 'https://github.com/netflix/lemur'

    def create_certificate(self, csr, issuer_options):
        """
        Creates a Verisign certificate.

        :param csr:
        :param issuer_options:
        :return: :raise Exception:
        """
#         url = current_app.config.get("VERISIGN_URL") + '/enroll'
#
#         data = process_options(issuer_options)
#         data['csr'] = csr
#
#         current_app.logger.info("Requesting a new verisign certificate: {0}".format(data))
#
#         response = self.session.post(url, data=data)
#         cert = handle_response(response.content)['Response']['Certificate']
#         return cert, constants.VERISIGN_INTERMEDIATE,
        print "I am in Create_certificate"

    @staticmethod
    def create_authority(options):
        """
        Creates an authority, this authority is then used by Lemur to allow a user
        to specify which Certificate Authority they want to sign their certificate.

        :param options:
        :return:
        """
        role = {'username': '', 'password': '', 'name': 'digicert'}
        return constants.DIGICERT_ROOT, "", [role]

