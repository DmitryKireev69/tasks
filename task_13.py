import time
import functools
from typing import Callable
from collections import OrderedDict


def cached(max_size: int = None, seconds: int = None):
    """
    Декоратор для кэширования результатов функции

    :param max_size: максимальное количество записей в кэше
    :param seconds: время жизни записей в секундах
    """

    def decorator(func: Callable) -> Callable:
        max_size_val = None if not isinstance(max_size, int) or max_size <= 0 else max_size
        seconds_val = None if not isinstance(seconds, (int, float)) or seconds <= 0 else seconds

        cache = OrderedDict()

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> any:
            key = (args, tuple(sorted(kwargs.items())))
            current_time: float = time.time()
            if key in cache:
                result, timestamp = cache[key]
                if seconds_val is not None and (current_time - timestamp) > seconds_val:
                    del cache[key]
                else:
                    cache.move_to_end(key)
                    return result

            result = func(*args, **kwargs)
            cache[key] = (result, current_time)

            if max_size_val is not None and len(cache) > max_size_val:
                cache.popitem(last=False)

            return result

        def clear_cache() -> None:
            """Очищает весь кэш."""
            cache.clear()

        def get_cache_size() -> int:
            """Возвращает текущий размер кэша."""
            return len(cache)

        def get_cache_info() -> dict[str, any]:
            """Возвращает информацию о кэше."""
            return {
                "size": len(cache),
                "max_size": max_size_val,
                "ttl": seconds_val,
                "function": func.__name__
            }

        wrapper.clear_cache = clear_cache
        wrapper.get_cache_size = get_cache_size
        wrapper.get_cache_info = get_cache_info
        return wrapper
    return decorator
