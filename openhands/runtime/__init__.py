from openhands.runtime.e2b.sandbox import E2BBox


def get_runtime_cls(name: str):
    # Local imports to avoid circular imports
    if name == 'eventstream':
        from openhands.runtime.client.runtime import EventStreamRuntime

        return EventStreamRuntime
    elif name == 'e2b':
        from openhands.runtime.e2b.runtime import E2BRuntime

        return E2BRuntime
    else:
        raise ValueError(f'Runtime {name} not supported')


__all__ = [
    'E2BBox',
    'get_runtime_cls',
]
