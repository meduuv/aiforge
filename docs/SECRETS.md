# Secret handling

API keys and provider credentials belong in environment variables or a dedicated secret store, never in source files.

Logs should redact authorization headers, tokens, and credentials. Rotate credentials immediately if they are accidentally committed.
