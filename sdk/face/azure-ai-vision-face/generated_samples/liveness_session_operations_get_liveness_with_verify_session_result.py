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
    python liveness_session_operations_get_liveness_with_verify_session_result.py
"""


def main():
    client = FaceAdministrationClient(
        endpoint="ENDPOINT",
        credential="CREDENTIAL",
    )

    response = client.get_liveness_with_verify_session_result(
        session_id="b12e033e-bda7-4b83-a211-e721c661f30e",
    )
    print(response)


if __name__ == "__main__":
    main()
