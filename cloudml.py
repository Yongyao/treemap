#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 13:02:09 2018

@author: yjiang
"""

import os
from oauth2client.client import GoogleCredentials
from googleapiclient import discovery

def predict_json(project, model, instances, version=None):
    """Send json data to a deployed model for prediction.
    Args:
        project (str): project where the Cloud ML Engine Model is deployed.
        model (str): model name.
        instances ([[float]]): List of input instances, where each input
           instance is a list of floats.
        version: str, version of the model to target.
    Returns:
        Mapping[str: any]: dictionary of prediction results defined by the
            model.
    """
    # Create the ML Engine service object.
    # To authenticate set the environment variable
    # GOOGLE_APPLICATION_CREDENTIALS=<path_to_service_account_file>
    service = discovery.build('ml', 'v1')
    name = 'projects/{}/models/{}'.format(project, model)

    if version is not None:
        name += '/versions/{}'.format(version)

    response = service.projects().predict(
        name=name,
        body={'instances': instances}
    ).execute()
    

    if 'error' in response:
        raise RuntimeError(response['error'])

    return response['predictions']

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/yjiang/Downloads/gcp/key/EOTest-0376c836fff3.json'
instances = [[6.8,  2.8,  4.8,  1.9], [6.0,  3.4,  0.5,  1.6]]
# instances = [[1.0], [2.0], [3.0], [4.0]]
test = predict_json('eotest-207015', 'landsat', instances)
print test