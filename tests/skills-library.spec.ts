import { test, expect } from "@playwright/test";
import * as fs from "fs";
import * as path from "path";
import * as yaml from "yaml";

const SKILLS_DIR = path.join(__dirname, "..", "skills");
const REGISTRY_PATH = path.join(__dirname, "..", "registry.json");
const PLUGIN_PATH = path.join(__dirname, "..", "plugin.json");

// Helper: collect all SKILL.md paths
function getAllSkillPaths(): string[] {
  const paths: string[] = [];
  const domains = fs.readdirSync(SKILLS_DIR);
  for (const domain of domains) {
    const domainPath = path.join(SKILLS_DIR, domain);
    if (!fs.statSync(domainPath).isDirectory()) continue;
    const skills = fs.readdirSync(domainPath);
    for (const skill of skills) {
      const skillFile = path.join(domainPath, skill, "SKILL.md");
      if (fs.existsSync(skillFile)) {
        paths.push(skillFile);
      }
    }
  }
  return paths.sort();
}

// Helper: parse YAML frontmatter from a SKILL.md file
function parseFrontmatter(filePath: string): Record<string, unknown> {
  const content = fs.readFileSync(filePath, "utf-8");
  if (!content.startsWith("---")) throw new Error(`No frontmatter: ${filePath}`);
  const endIdx = content.indexOf("---", 3);
  if (endIdx === -1) throw new Error(`No closing ---: ${filePath}`);
  const fmText = content.slice(3, endIdx);
  return yaml.parse(fmText) as Record<string, unknown>;
}

test.describe("Skill Discovery", () => {
  test("finds exactly 107 SKILL.md files", () => {
    const paths = getAllSkillPaths();
    expect(paths.length).toBe(107);
  });

  test("skills span exactly 14 domains", () => {
    const domains = fs.readdirSync(SKILLS_DIR).filter((d) =>
      fs.statSync(path.join(SKILLS_DIR, d)).isDirectory()
    );
    expect(domains.length).toBe(14);
  });

  test("every SKILL.md has valid YAML frontmatter", () => {
    const paths = getAllSkillPaths();
    for (const p of paths) {
      expect(() => parseFrontmatter(p)).not.toThrow();
    }
  });

  test("every SKILL.md has Agent Skills v2 name field", () => {
    const paths = getAllSkillPaths();
    for (const p of paths) {
      const fm = parseFrontmatter(p);
      expect(fm.name).toBeTruthy();
      expect(typeof fm.name).toBe("string");
      expect((fm.name as string).length).toBeLessThanOrEqual(64);
      expect(fm.name).toMatch(/^[a-z0-9-]+$/);
    }
  });

  test("every SKILL.md has description <= 250 chars", () => {
    const paths = getAllSkillPaths();
    for (const p of paths) {
      const fm = parseFrontmatter(p);
      expect(fm.description).toBeTruthy();
      expect(typeof fm.description).toBe("string");
      expect((fm.description as string).length).toBeLessThanOrEqual(250);
    }
  });

  test("every SKILL.md has disable-model-invocation boolean", () => {
    const paths = getAllSkillPaths();
    for (const p of paths) {
      const fm = parseFrontmatter(p);
      expect(typeof fm["disable-model-invocation"]).toBe("boolean");
    }
  });

  test("every SKILL.md preserves existing required fields", () => {
    const paths = getAllSkillPaths();
    const requiredFields = ["skill_id", "skill_name", "domain", "evidence_strength"];
    for (const p of paths) {
      const fm = parseFrontmatter(p);
      for (const field of requiredFields) {
        expect(fm[field]).toBeTruthy();
      }
    }
  });
});

test.describe("Registry Validation", () => {
  let registry: {
    version: string;
    standard: string;
    total_skills: number;
    domains: Array<{ id: string; label: string; skill_count: number }>;
    skills: Array<{
      id: string;
      name: string;
      description: string;
      disable_model_invocation: boolean;
      path: string;
      domain: string;
      chain_edges: {
        receives_from: unknown[];
        feeds_into: unknown[];
        output_field: unknown;
        input_field: unknown;
      };
    }>;
  };

  test.beforeAll(() => {
    const content = fs.readFileSync(REGISTRY_PATH, "utf-8");
    registry = JSON.parse(content);
  });

  test("registry.json is valid JSON with correct version", () => {
    expect(registry.version).toBe("2.0");
    expect(registry.standard).toBe("agent-skills-1.0");
  });

  test("registry contains 107 skills", () => {
    expect(registry.total_skills).toBe(107);
    expect(registry.skills.length).toBe(107);
  });

  test("registry contains 14 domains", () => {
    expect(registry.domains.length).toBe(14);
  });

  test("all descriptions are <= 250 characters", () => {
    for (const s of registry.skills) {
      expect(s.description.length).toBeLessThanOrEqual(250);
    }
  });

  test("all paths start with skills/ and point to existing files", () => {
    for (const s of registry.skills) {
      expect(s.path).toMatch(/^skills\//);
      const fullPath = path.join(__dirname, "..", s.path);
      expect(fs.existsSync(fullPath)).toBe(true);
    }
  });

  test("disable_model_invocation is boolean for all skills", () => {
    for (const s of registry.skills) {
      expect(typeof s.disable_model_invocation).toBe("boolean");
    }
  });

  test("chain_edges fields are null placeholders in v2", () => {
    for (const s of registry.skills) {
      expect(s.chain_edges.output_field).toBeNull();
      expect(s.chain_edges.input_field).toBeNull();
    }
  });

  test("domain skill counts match actual skill entries", () => {
    const counts: Record<string, number> = {};
    for (const s of registry.skills) {
      counts[s.domain] = (counts[s.domain] || 0) + 1;
    }
    for (const d of registry.domains) {
      expect(counts[d.id]).toBe(d.skill_count);
    }
  });

  test("registry matches SKILL.md files on disk", () => {
    const diskPaths = getAllSkillPaths().map((p) =>
      path.relative(path.join(__dirname, ".."), p)
    );
    const registryPaths = registry.skills.map((s) => s.path);
    expect(registryPaths.sort()).toEqual(diskPaths.sort());
  });
});

test.describe("Plugin Manifest Validation", () => {
  let plugin: {
    name: string;
    display_name: string;
    version: string;
    skills: string;
    license: string;
  };

  test.beforeAll(() => {
    const content = fs.readFileSync(PLUGIN_PATH, "utf-8");
    plugin = JSON.parse(content);
  });

  test("plugin.json is valid JSON", () => {
    expect(plugin.name).toBe("claude-education-skills");
    expect(plugin.version).toBe("2.0.0");
  });

  test("plugin.json skills directory exists", () => {
    const skillsDir = path.join(__dirname, "..", plugin.skills);
    expect(fs.existsSync(skillsDir)).toBe(true);
    expect(fs.statSync(skillsDir).isDirectory()).toBe(true);
  });

  test("plugin.json has correct license", () => {
    expect(plugin.license).toBe("CC BY-SA 4.0");
  });
});

test.describe("Backward Compatibility", () => {
  test("MCP server list_skills endpoint responds", async ({ request }) => {
    const response = await request.post("/mcp", {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json, text/event-stream",
      },
      data: {
        jsonrpc: "2.0",
        id: 1,
        method: "tools/list",
      },
    });
    expect(response.status()).toBe(200);
    const body = await response.json();
    expect(body.result).toBeTruthy();
    expect(body.result.tools).toBeTruthy();
    expect(body.result.tools.length).toBeGreaterThan(0);
  });
});
