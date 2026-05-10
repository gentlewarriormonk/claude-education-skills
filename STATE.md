# STATE.md — education-agent-skills

**Last updated:** 2026-05-10

## What was done

### Rename: claude-education-skills → education-agent-skills
- GitHub repo renamed (done outside this session)
- All 19 files updated (package.json, mcp-server/*, .claude-plugin/*, docs/*, tests/*, README.md, etc.)
- .codex-plugin/plugin.json created for OpenAI Codex support
- AGENTS.md created for coding agent repo guidance

### Tests fixed
- Test count assertions updated from 107/14 to 131/17 (actual counts from disk)
- Added missing `skills` field to .claude-plugin/plugin.json (was causing test failure)
- All 20 tests pass

### README restructured
- New "Get Started" section placed immediately after intro/badges
- Platform-equal structure: Claude, OpenAI Codex, Any Agent Skills tool, Manual
- Removed "Using the Library" (Claude-specific, now merged into Get Started)
- Removed "What Changed in v2" (moved to CHANGELOG.md)
- Removed "Install as Agent Skills" (merged into Get Started)
- CHANGELOG.md created with v3.0 and v2.0 entries

## What was verified
- `npx playwright test` → 20 passed, 0 failed
- No remaining references to "claude-education-skills" outside node_modules
- README structure confirmed readable

## Current state
- 131 skills across 17 domains
- All tests green
- Live MCP server: mcp-server-sigma-sooty.vercel.app/mcp
- CoWork plugin: .claude-plugin/plugin.json
- Codex plugin: .codex-plugin/plugin.json

## What's next
- No outstanding tasks
