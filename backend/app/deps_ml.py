from libs.ml_sdk import search_items, get_item

async def ml_search(query: str, price: str | None = None):
    return await search_items(query, price)

async def ml_item(item_id: str):
    return await get_item(item_id)
