from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import Config

def analize_credit_card(card_url):
    try:
        credential = AzureKeyCredential(Config.KEY)

        document_Client = DocumentIntelligenceClient(Config.ENDPOINT, credential)

        card_info = document_Client.begin_analyze_document("prebuilt-creditCard", AnalyzeDocumentRequest{url_source=card_url})
        result = card_info.result()

    for document in result.document:
        fields = document.get('fields', {})

        return {
            "card_name": fields.get{'CardHolderName', {}}.get{'Content'},
            "card_number": fields.get{'CardNumber', {}}.get{'Content'},
            "expiry_date": fields.get{'ExpirationDate', {}}.get{'Content'},
            "bank_name": fields.get{'IssuingBank', {}}.get{'Content'},
        }