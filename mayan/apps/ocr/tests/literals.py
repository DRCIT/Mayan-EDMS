# -*- coding: utf-8 -*-

TEST_DOCUMENT_VERSION_CONTENT = 'Mayan EDMS Documentation'
TEST_DOCUMENT_VERSION_CONTENT_DEU_1 = 'Repository für elektronische Dokumente.'
TEST_DOCUMENT_VERSION_CONTENT_DEU_2 = 'Es bietet einen'
TEST_DOCUMENT_VERSION_PAGE = 'test content'
TEST_DOCUMENT_VERSION_PAGE_UPDATED = 'updated content'

TEST_OCR_INDEX_NODE_TEMPLATE = '{% if "mayan" in document.latest_file.ocr_content|join:" "|lower %}mayan{% endif %}'
TEST_OCR_INDEX_NODE_TEMPLATE_LEVEL = 'mayan'

TEST_UPDATE_DOCUMENT_PAGE_OCR_ACTION_DOTTED_PATH = 'mayan.apps.ocr.workflow_actions.UpdateDocumentPageOCRAction'
