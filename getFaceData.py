#!/usr/bin/env python

# Copyright 2015 Google, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Draws squares around faces in the given image."""

import argparse
import base64

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from PIL import Image



# [START get_vision_service]
def get_vision_service():
    credentials = GoogleCredentials.get_application_default()
    return discovery.build('vision', 'v1', credentials=credentials)
# [END get_vision_service]


def detect_emotions(face_file, max_results=2):
    """Uses the Vision API to detect emotion of faces in the given file.
    Args:
        face_file: A file-like object containing an image with faces.
    Returns:
        An array of dicts with information about the emotion faces in the picture.
    """
    image_content = face_file.read()
    batch_request = [{
        'image': {
            'content': base64.b64encode(image_content).decode('utf-8')
            },
        'features': [{
            'type': 'FACE_DETECTION',
            'maxResults': max_results,
            }]
        }]

    service = get_vision_service()
    request = service.images().annotate(body={
        'requests': batch_request,
        })
    response = request.execute()

    faces=response['responses'][0]['faceAnnotations']

    likelihoods = ['joyLikelihood', 'sorrowLikelihood', 'angerLikelihood', 'surpriseLikelihood']
    emos = []  # make a list for extracting the likelihoods ( stored in dictionaries

    #extract the likelihoods and return as a list of 1 or 2 dictionaries
    for face in faces:
        for i in range(len(faces)):
            emos.append({key: face[key] for key in likelihoods})
    print(emos)
    return emos


def main(input_filename, max_results):
    with open(input_filename, 'rb') as image:
        faces = detect_emotions(image, max_results)
        print('Found {} face{}'.format(
            len(faces), '' if len(faces) == 1 else 's'))


        # Reset the file pointer, so we can read the file again
        image.seek(0)
        #emotions=face_emotions(faces)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Detects faces in the given image.')
    parser.add_argument(
        'input_image', help='the image you\'d like to detect faces in.')
    parser.add_argument(
        '--max-results', dest='max_results', default=2,
        help='the max results of face detection.')
    args = parser.parse_args()

    main(args.input_image, args.max_results)