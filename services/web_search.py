from duckduckgo_search import DDGS

def search_agricultural_web(query: str, crop: str = "", max_results: int = 3):
    """Perform a live web search for agricultural advice and farming solutions with fast timeout."""
    q_lower = query.lower()
    is_non_crop = any(k in q_lower for k in ["వర్షం", "వాతావరణం", "rain", "weather", "పీఎం కిసాన్", "రైతు భరోసా", "పథకం", "status", "జీవామృతం"])
    if crop and not is_non_crop:
        search_terms = f"{crop} {query} agriculture Vijayawada Andhra Pradesh"
    else:
        search_terms = f"{query} agriculture Vijayawada Andhra Pradesh"

    try:
        with DDGS(timeout=1.8) as ddgs:
            results = list(ddgs.text(search_terms, max_results=max_results))
        
        parsed = []
        for r in results:
            parsed.append({
                "title": r.get("title", ""),
                "snippet": r.get("body", ""),
                "url": r.get("href", "")
            })
        return parsed
    except Exception:
        return []
