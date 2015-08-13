import requests
import json
import sys
import time
from requests.auth import HTTPBasicAuth
from requests import Request, Session
from displays_cert import Retrieve_Issued_Certificate
from displays_cert import View_order_details


def Request_CSR():

    # reads the cert from a file
    #text_csr = open("/Users/keval/PycharmProjects/untitled1/server.csr", "r")
    text_csr = open("/Users/keval/server.csr", "r")
    csr = text_csr.read()
    print csr

    print("check 1")
    # setup auth
    # auth = HTTPBasicAuth("079962","gtphzqnmb6b4jdw1xsrvfg4nrl2jrdd2")
    auth = HTTPBasicAuth("120865","x7t0mgmlr9f9wqnxxpqw1mxb7qthwtzs")
    print("check 2")
    payload = {
      "type": "private_ssl",
      "org_unit": "abcd",
      "server_type": "2",
      "common_name": "test.opendns.com",
      "sans": "test.opendns.com",
      "comments": "test",
      "org_name": "Test - OpenDNS",
      "org_addr1": "378 Townsend",
      "org_addr2": "I am here",
      "org_city": "San Francisco",
      "org_state": "CA",
      "org_zip": "94107",
      "org_country": "US",
      "validity": "3",
      #"csr": "-----BEGIN CERTIFICATE REQUEST-----\n"+csr+"\n-----END CERTIFICATE REQUEST-----"
      "csr": csr
    }
    print("check 3")
    #post request to request for new SSL cert
    head = {'Content-Type': 'application/vnd.digicert.rest-v1+json'}
    r = requests.post("https://api.digicert.com/enterprise/certificate/ssl", data=json.dumps(payload), auth=auth, headers=head)
    print("check 4")
    requestid = r.json()["request_id"]
    print requestid
    return requestid

def View_CSR_request(req_id):

    # auth = HTTPBasicAuth("079962","gtphzqnmb6b4jdw1xsrvfg4nrl2jrdd2")
    auth = HTTPBasicAuth("120865","x7t0mgmlr9f9wqnxxpqw1mxb7qthwtzs")
    url1 = "https://api.digicert.com/request/"+req_id
    head = {'Content-Type': 'application/vnd.digicert.rest-v1+json'}
    myrequest = requests.get(url1, auth = auth, headers=head).json()
    print ("Viewing the Request")
    print myrequest



def Approve_Certificate(req_id):

    # auth = HTTPBasicAuth("079962","gtphzqnmb6b4jdw1xsrvfg4nrl2jrdd2")
    auth = HTTPBasicAuth("120865","x7t0mgmlr9f9wqnxxpqw1mxb7qthwtzs")
    head = {'Content-Type': 'application/vnd.digicert.rest-v1+json'}
    url = "https://api.digicert.com/request/"+req_id
    s = Session()
    req = Request('APPROVE', url,auth=auth,
        headers=head
    )
    prepped = req.prepare()
    print prepped
    print req

    orderid = s.send(prepped).json()["order_id"]
    print orderid

    return orderid


def Reject_Certificate(req_id):

    # auth = HTTPBasicAuth("079962","gtphzqnmb6b4jdw1xsrvfg4nrl2jrdd2")
    auth = HTTPBasicAuth("120865","x7t0mgmlr9f9wqnxxpqw1mxb7qthwtzs")
    head = {'Content-Type': 'application/vnd.digicert.rest-v1+json'}
    url = "https://api.digicert.com/request/"+req_id
    payload = {
      "note":"Request for new cert is not approved!"
    }
    s = Session()
    req = Request('REJECT', url,auth=auth,data=json.dumps(payload),
        headers=head
    )
    prepped = req.prepare()
    print prepped
    print req

    resp = s.send(prepped
    ).json()
    print resp


## Starts Here---
request_id = Request_CSR()
View_CSR_request(request_id)

choice = raw_input("Choose the correct option 'A to APPROVE' or 'R to REJECT' certificate\n")
if choice == ('A' or 'a'):
    cert_orderid = Approve_Certificate(request_id)

    option = raw_input("Choose the correct option 'V to view-order-details' or 'R to Retrieve-Issued-Cert' certificate\n")
    if option == ('V' or 'v'):
        print"Waiting for processes to complete...30 seconds"
        time.sleep(50)
        View_order_details(cert_orderid)
    else:
        print "Invalid option"

    option = raw_input("Choose the correct option 'V to view-order-details' or 'R to Retrieve-Issued-Cert' certificate\n")

    if option == ('R' or 'r'):
        print"Waiting for processes to complete...10 seconds"
        time.sleep(10)
        x,y,z,zz,o = Retrieve_Issued_Certificate(cert_orderid)

        print "================================================"
        print "\n"
        print x
        print y
        print z
        print zz
        print o
        name1 = o+'-server-cert'+'.txt'
        my_file = open(name1, "w")
        my_file.write(x)
        my_file.close()

        name2 = o+'-intermediate-cert'+'.txt'
        my_file = open(name2, "w")
        my_file.write(y)
        my_file.close()

        name3 = o+'-root-cert'+'.txt'
        my_file = open(name3, "w")
        my_file.write(z)
        my_file.close()

        name4 = o+'-pkcs7'+'.txt'
        my_file = open(name4, "w")
        my_file.write(zz)
        my_file.close()

    else:
        print "Invalid option"



elif choice == ('R' or 'r'):
    Reject_Certificate(request_id)
else:
    print ("Invalid Option\n")
