# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import pytest
import functools
from devtools_testutils.aio import recorded_by_proxy_async
from devtools_testutils import set_bodiless_matcher
from azure.ai.formrecognizer.aio import DocumentAnalysisClient, DocumentModelAdministrationClient
from azure.ai.formrecognizer._generated.v2023_07_31.models import AnalyzeResultOperation
from azure.ai.formrecognizer import AnalyzeResult
from preparers import FormRecognizerPreparer, get_async_client
from asynctestcase import AsyncFormRecognizerTest
from conftest import skip_flaky_test

get_dma_client = functools.partial(get_async_client, DocumentModelAdministrationClient)
get_da_client = functools.partial(get_async_client, DocumentAnalysisClient)

class TestDACAnalyzeCustomModelFromUrlAsync(AsyncFormRecognizerTest):

    @FormRecognizerPreparer()
    async def test_document_analysis_none_model(self, **kwargs):
        client = get_da_client()
        with pytest.raises(ValueError) as e:
            async with client:
                await client.begin_analyze_document_from_url(model_id=None, document_url="https://badurl.jpg")
        assert "model_id cannot be None or empty." in str(e.value)

    @FormRecognizerPreparer()
    async def test_document_analysis_empty_model_id(self, **kwargs):
        client = get_da_client()
        with pytest.raises(ValueError) as e:
            async with client:
                await client.begin_analyze_document_from_url(model_id="", document_url="https://badurl.jpg")
        assert "model_id cannot be None or empty." in str(e.value)

    @skip_flaky_test
    @FormRecognizerPreparer()
    @recorded_by_proxy_async
    async def test_custom_document_selection_mark(self, formrecognizer_selection_mark_storage_container_sas_url, **kwargs):
        client = get_dma_client()
        set_bodiless_matcher()
        da_client = client.get_document_analysis_client()

        responses = []

        def callback(raw_response, _, headers):
            analyze_result = da_client._deserialize(AnalyzeResultOperation, raw_response)
            document = AnalyzeResult._from_generated(analyze_result.analyze_result)
            responses.append(analyze_result)
            responses.append(document)

        async with client:
            poller = await client.begin_build_document_model("template", blob_container_url=formrecognizer_selection_mark_storage_container_sas_url)
            model = await poller.result()
            poller = await da_client.begin_analyze_document_from_url(
                model_id=model.model_id,
                document_url=self.selection_mark_url_pdf,
                cls=callback
            )
            document = await poller.result()
        raw_analyze_result = responses[0].analyze_result
        returned_model = responses[1]

        # Check AnalyzeResult
        assert returned_model.model_id == raw_analyze_result.model_id
        assert returned_model.api_version == raw_analyze_result.api_version
        assert returned_model.content == raw_analyze_result.content

        self.assertDocumentPagesTransformCorrect(returned_model.pages, raw_analyze_result.pages)
        self.assertDocumentTransformCorrect(returned_model.documents, raw_analyze_result.documents)
        self.assertDocumentTablesTransformCorrect(returned_model.tables, raw_analyze_result.tables)
        self.assertDocumentKeyValuePairsTransformCorrect(returned_model.key_value_pairs, raw_analyze_result.key_value_pairs)
        self.assertDocumentStylesTransformCorrect(returned_model.styles, raw_analyze_result.styles)

        # check page range
        assert len(raw_analyze_result.pages) == len(returned_model.pages)

    @skip_flaky_test
    @FormRecognizerPreparer()
    @recorded_by_proxy_async
    async def test_label_tables_variable_rows(self, formrecognizer_table_variable_rows_container_sas_url, **kwargs):
        client = get_dma_client()
        set_bodiless_matcher()
        da_client = client.get_document_analysis_client()

        responses = []

        def callback(raw_response, _, headers):
            analyze_result = da_client._deserialize(AnalyzeResultOperation, raw_response)
            document = AnalyzeResult._from_generated(analyze_result.analyze_result)
            responses.append(analyze_result)
            responses.append(document)

        async with client:
            build_poller = await client.begin_build_document_model(
                "template", blob_container_url=formrecognizer_table_variable_rows_container_sas_url)
            model = await build_poller.result()

            poller = await da_client.begin_analyze_document_from_url(
                model.model_id,
                self.label_table_variable_row_url_pdf,
                cls=callback
            )
            document = await poller.result()

        raw_analyze_result = responses[0].analyze_result
        returned_model = responses[1]

        # Check AnalyzeResult
        assert returned_model.model_id == raw_analyze_result.model_id
        assert returned_model.api_version == raw_analyze_result.api_version
        assert returned_model.content == raw_analyze_result.content

        self.assertDocumentPagesTransformCorrect(returned_model.pages, raw_analyze_result.pages)
        self.assertDocumentTransformCorrect(returned_model.documents, raw_analyze_result.documents)
        self.assertDocumentTablesTransformCorrect(returned_model.tables, raw_analyze_result.tables)
        self.assertDocumentKeyValuePairsTransformCorrect(returned_model.key_value_pairs, raw_analyze_result.key_value_pairs)
        self.assertDocumentStylesTransformCorrect(returned_model.styles, raw_analyze_result.styles)

        # check page range
        assert len(raw_analyze_result.pages) == len(returned_model.pages)

    @skip_flaky_test
    @FormRecognizerPreparer()
    @recorded_by_proxy_async
    async def test_label_tables_fixed_rows(self, formrecognizer_table_fixed_rows_container_sas_url, **kwargs):
        client = get_dma_client()
        set_bodiless_matcher()
        da_client = client.get_document_analysis_client()

        responses = []

        def callback(raw_response, _, headers):
            analyze_result = da_client._deserialize(AnalyzeResultOperation, raw_response)
            document = AnalyzeResult._from_generated(analyze_result.analyze_result)
            responses.append(analyze_result)
            responses.append(document)

        async with client:
            build_poller = await client.begin_build_document_model("template", blob_container_url=formrecognizer_table_fixed_rows_container_sas_url)
            model = await build_poller.result()

            poller = await da_client.begin_analyze_document_from_url(
                model.model_id,
                self.label_table_fixed_row_url_pdf,
                cls=callback
            )
            form = await poller.result()

        raw_analyze_result = responses[0].analyze_result
        returned_model = responses[1]

        # Check AnalyzeResult
        assert returned_model.model_id == raw_analyze_result.model_id
        assert returned_model.api_version == raw_analyze_result.api_version
        assert returned_model.content == raw_analyze_result.content

        self.assertDocumentPagesTransformCorrect(returned_model.pages, raw_analyze_result.pages)
        self.assertDocumentTransformCorrect(returned_model.documents, raw_analyze_result.documents)
        self.assertDocumentTablesTransformCorrect(returned_model.tables, raw_analyze_result.tables)
        self.assertDocumentKeyValuePairsTransformCorrect(returned_model.key_value_pairs, raw_analyze_result.key_value_pairs)
        self.assertDocumentStylesTransformCorrect(returned_model.styles, raw_analyze_result.styles)

        # check page range
        assert len(raw_analyze_result.pages) == len(returned_model.pages)
