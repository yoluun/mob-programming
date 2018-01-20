#fbapi
from fbkey import *
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json, sys


def detectFaces(img):


	return 0

def createPersonGroup(personGroupId, name, userData=None):
	#CREATE PERSON GROUP

# Replace 'examplegroupid' with an ID you haven't used for creating a group before.
# The valid characters for the ID include numbers, English letters in lower case, '-' and '_'. 
# The maximum length of the ID is 64.
#personGroupId = 'georgesung'

# The userData field is optional. The size limit for it is 16KB.
#body = "{ 'name':'GeorgeTan', 'userData':'abcdefg' }"
body = "{'name':'" + name +"', 'userData':'" + userData + "'}"

try:
    # NOTE: You must use the same location in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westus, replace "westcentralus" in the 
    #   URL below with "westus".
    conn = http.client.HTTPSConnection(uri_base.strip('https://'))
    conn.request("PUT", "/face/v1.0/persongroups/%s" % personGroupId, body, headers)
    response = conn.getresponse()

    # 'OK' indicates success. 'Conflict' means a group with this ID already exists.
    # If you get 'Conflict', change the value of personGroupId above and try again.
    # If you get 'Access Denied', verify the validity of the subscription key above and try again.
    return response.reason

    conn.close()
except Exception as e:
    return(e.args)
####################################
 

def createPerson(personGroupId, name, userData=None):
	return 0 

def applyFace(personGroupId, personId, image):
	return 0 

def verifyFace(image, personGroupId=None, personId=None):
	return 0 