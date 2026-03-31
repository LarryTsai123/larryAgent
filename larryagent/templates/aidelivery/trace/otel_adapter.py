def emit_span(name: str, attributes: dict | None = None) -> dict:
    return {
        "span_name": name,
        "attributes": attributes or {}
    }
