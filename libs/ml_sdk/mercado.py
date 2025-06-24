import httpx

BASE_URL = "https://api.mercadolibre.com"
SITE_ID = "MLC"

async def search_items(query: str, price: str = None):
    params = {"q": query, "limit": 20}
    if price:
        params["price"] = price
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        r = await client.get(f"/sites/{SITE_ID}/search", params=params)
        r.raise_for_status()
        return r.json()

async def get_item(item_id: str):
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        r = await client.get(f"/items/{item_id}")
        r.raise_for_status()
        return r.json()

async def refresh_token(refresh_token: str):
    # Placeholder for OAuth refresh logic
    return {"access_token": "test", "refresh_token": refresh_token}
