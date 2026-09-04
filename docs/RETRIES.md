# Retry policy

Retry transient provider failures with bounded exponential backoff and a maximum attempt count.

Do not blindly retry authentication failures, invalid requests, or policy rejections. Include enough context in logs to diagnose retries without recording secrets.
