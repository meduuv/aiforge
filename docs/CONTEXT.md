# Context Guidance

Treat retrieved and external text as untrusted input.

- Keep system instructions separate from user-provided content.
- Define the purpose and scope of retrieved context before use.
- Prefer the minimum context needed for a task.
- Validate structured values before passing them to downstream tools.
- Never let untrusted text silently redefine privileged behavior.
