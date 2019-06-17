# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class StoredImagePrediction(Model):
    """result of an image classification request.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar resized_image_uri: The URI to the (resized) prediction image.
    :vartype resized_image_uri: str
    :ivar thumbnail_uri: The URI to the thumbnail of the original prediction
     image.
    :vartype thumbnail_uri: str
    :ivar original_image_uri: The URI to the original prediction image.
    :vartype original_image_uri: str
    :ivar domain: Domain used for the prediction.
    :vartype domain: str
    :ivar id: Prediction Id.
    :vartype id: str
    :ivar project: Project Id.
    :vartype project: str
    :ivar iteration: Iteration Id.
    :vartype iteration: str
    :ivar created: Date this prediction was created.
    :vartype created: datetime
    :ivar predictions: List of predictions.
    :vartype predictions:
     list[~azure.cognitiveservices.vision.customvision.training.models.Prediction]
    """

    _validation = {
        'resized_image_uri': {'readonly': True},
        'thumbnail_uri': {'readonly': True},
        'original_image_uri': {'readonly': True},
        'domain': {'readonly': True},
        'id': {'readonly': True},
        'project': {'readonly': True},
        'iteration': {'readonly': True},
        'created': {'readonly': True},
        'predictions': {'readonly': True},
    }

    _attribute_map = {
        'resized_image_uri': {'key': 'resizedImageUri', 'type': 'str'},
        'thumbnail_uri': {'key': 'thumbnailUri', 'type': 'str'},
        'original_image_uri': {'key': 'originalImageUri', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'project': {'key': 'project', 'type': 'str'},
        'iteration': {'key': 'iteration', 'type': 'str'},
        'created': {'key': 'created', 'type': 'iso-8601'},
        'predictions': {'key': 'predictions', 'type': '[Prediction]'},
    }

    def __init__(self, **kwargs):
        super(StoredImagePrediction, self).__init__(**kwargs)
        self.resized_image_uri = None
        self.thumbnail_uri = None
        self.original_image_uri = None
        self.domain = None
        self.id = None
        self.project = None
        self.iteration = None
        self.created = None
        self.predictions = None