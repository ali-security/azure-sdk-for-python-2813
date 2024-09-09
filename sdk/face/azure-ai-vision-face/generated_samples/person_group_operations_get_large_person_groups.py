# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.ai.vision.face import FaceAdministrationClient

"""
# PREREQUISITES
    pip install azure-ai-vision-face
# USAGE
    python person_group_operations_get_large_person_groups.py
"""


def main():
    client = FaceAdministrationClient(
        endpoint="ENDPOINT",
        credential="CREDENTIAL",
    )

    response = client.large_person_group.get_large_person_groups()
    print(response)


if __name__ == "__main__":
    main()
