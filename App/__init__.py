"""Shared HTTP access for the chart pages."""
from urllib.request import getproxies
from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def get_chart_response(url):
    proxies = getproxies()
    proxy = proxies.get("https", "")
    # Windows labels an HTTP localhost proxy as HTTPS for HTTPS destinations.
    if proxy.startswith(("https://127.0.0.1:", "https://localhost:")):
        proxies["https"] = "http://" + proxy[len("https://"):]
    with Session() as session:
        retry = Retry(total=2, backoff_factor=1, status_forcelist=(429, 500, 502, 503, 504), allowed_methods=("GET",))
        session.mount("https://", HTTPAdapter(max_retries=retry))
        response = session.get(url, proxies=proxies, timeout=(10, 25))
        response.raise_for_status()
        return response
