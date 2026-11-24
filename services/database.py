import os
from typing import Optional, Any

_SUPABASE_CLIENT = None

def get_supabase() -> Optional[Any]:
    """Return Supabase client if configured, otherwise None."""
    global _SUPABASE_CLIENT
    if _SUPABASE_CLIENT is not None:
        return _SUPABASE_CLIENT
    try:
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")

        if url and key and len(url.strip()) > 5 and len(key.strip()) > 5 and "placeholder" not in url.lower():
            from supabase import create_client
            _SUPABASE_CLIENT = create_client(url, key)
            return _SUPABASE_CLIENT
    except Exception:
        pass
    return None
