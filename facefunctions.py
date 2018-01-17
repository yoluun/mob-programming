#fbapi
from fbkey import *
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json, sys


def detectFaces(img_url):
	# Request headers.
	headers = {
		'Content-Type': 'application/json',
		'Ocp-Apim-Subscription-Key': subscription_key,
	}

	# Request parameters.
	params = {
		'returnFaceId': 'true',
		'returnFaceLandmarks': 'false',
		'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
	}

	# Body. The URL of a JPEG image to analyze.
	body = {'url': img_url}

	try:
		# Execute the REST API call and get the response.
		response = requests.request('POST', uri_base + '/face/v1.0/detect', json=body, data=None, headers=headers, params=params)

		parsed = json.loads(response.text)

	except Exception as e:
		print('Error:')
		print(e)
		return None

	return parsed

def createPersonGroup(personGroupId, name, userData=None):
	return 0

def createPerson(personGroupId, name, userData=None):
	return 0

def applyFace(personGroupId, personId, image):
	return 0

def verifyFace(image, personGroupId=None, personId=None):
	return 0
