from datetime import datetime

def build_app_new(api_key: str, client_id: str, *,
                  product_type: str = "Osago",
                  success_payment_url: str = "https://osago.ab.insapp.ru/success",
                  channel_type: str = "Widget",
                  local_time: str | None = None,
                  utm: str = "{}") -> dict:
    return {
        "apiKey": api_key,
        "productType": product_type,
        "successPaymentUrl": success_payment_url,
        "clientId": client_id,
        "channelType": channel_type,
        "localTime": local_time or datetime.now().isoformat(timespec="milliseconds"),
        "utm": utm,
    }

def build_simple(api_key: str, application_id: str, **extra) -> dict:
    """Универсальный билдер для SendToInsurers, GetOffers, SelectOffer, GetOsagoPaymentLink"""
    body = {"apiKey": api_key, "applicationId": application_id}
    body.update(extra)
    return body
