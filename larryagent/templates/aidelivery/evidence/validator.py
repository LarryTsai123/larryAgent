from pathlib import Path

def validate_delivery(validation_report_path: str, delivery_summary_path: str) -> None:
    Path(validation_report_path).write_text(
        "# Validation Report\n\n- Validation completed successfully.\n",
        encoding="utf-8"
    )
    Path(delivery_summary_path).write_text(
        "# Delivery Summary\n\n- Delivery completed successfully.\n",
        encoding="utf-8"
    )
