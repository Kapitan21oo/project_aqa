from qa_core.api.client import Client
import requests

def app_new(client: Client, payload: dict) -> requests.Response:
    return client.request("POST", "/app/new", json=payload)

def send_osago_application(client: Client, payload: dict) -> requests.Response:
    return client.request("POST", "/app/SendOsagoApplication", json=payload)

def send_to_insurers(client: Client, payload: dict) -> requests.Response:
    return client.request("POST", "/app/SendToInsurers", json=payload)

def get_offers(client: Client, payload: dict) -> requests.Response:
    return client.request("POST", "/app/GetOffers", json=payload)

def select_offer(client: Client, payload: dict) -> requests.Response:
    return client.request("POST", "/app/SelectOffer", json=payload)

def get_osago_payment_link(client: Client, payload: dict) -> requests.Response:
    return client.request("POST", "/app/GetOsagoPaymentLink", json=payload)
