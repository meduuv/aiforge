# Model Safety Notes

AIForge integrations should treat model output as untrusted data.

## Application boundaries

- Validate structured model output before using it.
- Keep secrets and credentials outside prompts and model-visible logs.
- Apply explicit timeouts and size limits to model requests.
- Do not execute generated code or shell commands without a separate authorization and validation layer.
- Log failures without recording sensitive prompt contents by default.

These guidelines are intended to reduce accidental privilege escalation, prompt injection impact, and unsafe automation behavior.