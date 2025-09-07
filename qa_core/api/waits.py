import time
from .client import Client
from .endpoint.main_process import get_offers, get_osago_payment_link


def wait_all_offers_received(client: Client, payload: dict,
                             timeout_s: int = 120, interval_s: int = 1) -> dict:
    """Ждём, пока GetOffers вернёт allOffersReceived == true."""
    deadline = time.monotonic() + timeout_s
    while time.monotonic() < deadline:
        resp = get_offers(client, payload)
        data = resp.json()
        if (data.get("value") or {}).get("allOffersReceived") is True:
            return data
        time.sleep(interval_s)
    raise TimeoutError(f"Не дождались офферов за {timeout_s} секунд")

def wait_payment_link_received(client: Client, payload: dict,
                               timeout_s: int = 120, interval_s: int = 1) -> str:
    """Ждём, пока GetOsagoPaymentLink вернёт статус Received и ссылку."""
    deadline = time.monotonic() + timeout_s
    while time.monotonic() < deadline:
        resp = get_osago_payment_link(client, payload)
        data = resp.json()
        value = data.get("value") or {}
        if value.get("status") == "Received" and value.get("osagoPaymentLink"):
            return value["osagoPaymentLink"]
        time.sleep(interval_s)
    raise TimeoutError(f"Не дождались ссылки оплаты за {timeout_s} секунд")
