# Changelog

## v3.0 — May 2026

- Renamed from `claude-education-skills` to `education-agent-skills`
- Added OpenAI Codex plugin support (`.codex-plugin/plugin.json`)
- Added `AGENTS.md` for coding agent repo guidance
- README restructured for model-agnostic positioning — works with Claude, Codex, and any Agent Skills-compatible tool
- 131 skills across 17 domains

## v2.0 — April 2026

The library became compliant with the **Agent Skills 1.0 open standard**. What this meant in practice:

- **One-command install** — no manual setup, no copy-pasting prompts
- **Progressive disclosure** — skill metadata loads first; full skill content loads only when activated, keeping context lean
- **Auto-activation** — skills trigger when your conversation matches their description, without explicit invocation
- **Machine-readable registry** — `registry.json` indexes all skills with descriptions, tags, chaining metadata, and domain grouping for programmatic consumption
- **Backward compatible** — the MCP server, direct prompt use, and all existing workflows continued to work unchanged
