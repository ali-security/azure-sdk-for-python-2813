#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
An example to show receiving events from an Event Hub with checkpoint store doing checkpoint by batch asynchronously.
In the `receive_batch` method of `EventHubConsumerClient`:
If no partition id is specified, the checkpoint_store are used for load-balance and checkpoint.
If partition id is specified, the checkpoint_store can only be used for checkpoint without load balancing.
"""

import asyncio
import os
import logging
from azure.eventhub.aio import EventHubConsumerClient
from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore
from azure.identity.aio import DefaultAzureCredential

FULLY_QUALIFIED_NAMESPACE = os.environ["EVENT_HUB_HOSTNAME"]
EVENTHUB_NAME = os.environ['EVENT_HUB_NAME']

storage_account_name = os.environ["AZURE_STORAGE_ACCOUNT"]
protocol = os.environ.get("PROTOCOL", "https")
suffix = os.environ.get("ACCOUNT_URL_SUFFIX", "core.windows.net")
BLOB_ACCOUNT_URL = f"{protocol}://{storage_account_name}.blob.{suffix}"
BLOB_CONTAINER_NAME = "your-blob-container-name"  # Please make sure the blob container resource exists.

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


async def batch_process_events(events):
    # put your code here
    await asyncio.sleep(2)  # simulate something I/O bound


async def on_event_batch(partition_context, event_batch):
    log.info("Partition {}, Received count: {}".format(partition_context.partition_id, len(event_batch)))
    await batch_process_events(event_batch)
    await partition_context.update_checkpoint()


async def receive_batch():
    checkpoint_store = BlobCheckpointStore(
        blob_account_url=BLOB_ACCOUNT_URL,
        container_name=BLOB_CONTAINER_NAME,
        credential=DefaultAzureCredential()
    )
    client = EventHubConsumerClient(
        fully_qualified_namespace=FULLY_QUALIFIED_NAMESPACE,
        eventhub_name=EVENTHUB_NAME,
        credential=DefaultAzureCredential(),
        consumer_group="$Default",
        checkpoint_store=checkpoint_store,
    )
    async with client:
        await client.receive_batch(
            on_event_batch=on_event_batch,
            max_batch_size=100,
            starting_position="-1",  # "-1" is from the beginning of the partition.
        )


if __name__ == '__main__':
    asyncio.run(receive_batch())
