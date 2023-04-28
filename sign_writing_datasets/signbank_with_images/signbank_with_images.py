"""SignBankWithImages dataset."""
import json
import os

import boto3

import tensorflow as tf
import tensorflow_datasets as tfds

from sign_writing_datasets.warning import dataset_warning
_CITATION = """
"""

_DESCRIPTION = """
SignBank Site: SignWriting Software for Sign Languages, including SignMaker 2017, 
SignPuddle Online, the SignWriting Character Viewer, SignWriting True Type Fonts, 
Delegs SignWriting Editor, SignBank Databases in FileMaker, SignWriting DocumentMaker, 
SignWriting Icon Server, the International SignWriting Alphabet (ISWA 2010) HTML Reference Guide, 
the ISWA 2010 Font Reference Library and the RAND Keyboard for SignWriting.
"""

BUCKET_NAME = 'signwriting-images'

class SignBankWithImages(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for SignBank dataset."""

    VERSION = tfds.core.Version("1.0.0")
    RELEASE_NOTES = {
        "1.0.0": "Initial release.",
    }

    def __init__(self, access_key: str, private_key: str, **kwargs):

        super(SignBankWithImages, self).__init__(**kwargs)

        self.client = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=private_key
        )

    def _info(self) -> tfds.core.DatasetInfo:
        """Returns the dataset metadata."""

        features = {
            "puddle": tf.int32,
            "id": tfds.features.Text(),
            "assumed_spoken_language_code": tfds.features.Text(),
            "country_code": tfds.features.Text(),
            "created_date": tfds.features.Text(),
            "modified_date": tfds.features.Text(),
            "sign_writing": tfds.features.Sequence(tfds.features.Sequence(tfds.features.Text())),
            "sign_writing_images": tfds.features.Sequence(tfds.features.Sequence(tfds.features.Text())),
            "terms": tfds.features.Sequence(tfds.features.Text()),
            "user": tfds.features.Text(),
        }

        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(features),
            homepage="http://signbank.org/",
            supervised_keys=None,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        dataset_warning(self)

        return {
            "train": self._generate_examples(
                samples=[key['Key'] for key in self.client.list_objects(Bucket=BUCKET_NAME)['Contents']]
            ),
        }

    def _generate_examples(self, samples: list[str]):
        for i, sample in enumerate(samples):
            obj = self.client.get_object(Bucket=BUCKET_NAME, Key=sample)['Body'].read().decode('utf-8')
            obj = json.loads(obj)
            yield i, obj
