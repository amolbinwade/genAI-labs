from fastapi import Request, HTTPException, status
import time
import threading

_lock = threading.Lock()
_last_call = {}
RATE_LIMIT_PERIOD_SECONDS = 60

def _get_client_id(request: Request) -> str:
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0].strip()
    if request.client:
        return request.client.host
    return "unknown"

def rate_limit(request: Request):
    """Dependency that allows one request per `period_seconds` per client.

    Notes:
    - This is an in-memory limiter (per process). For multi-worker deployments
      use a shared store like Redis.
    """
    period_seconds = RATE_LIMIT_PERIOD_SECONDS
    client = _get_client_id(request)
    now = time.time()
    with _lock:
        last = _last_call.get(client)
        if last is not None and (now - last) < period_seconds:
            retry_after = int(period_seconds - (now - last))
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded. Try again later.",
                headers={"Retry-After": str(retry_after)},
            )
        _last_call[client] = now
