---
created: 2026-07-02
seed_version: "7.0"
architecture_tier: "1_preset_osint"
---

# Vault Initial Configuration

## Domain
domain: "OSINT & Geopolitics"
languages: ["en", "it"]
persona: "Strategic Analyst"

## Infrastructure
platform: "claude_code"
primary_llm: "claude"
cost_optimization_mode: "false"
has_local_inference: "false"
deferred_agents: "false"
local_models: []

## Domain Parameters (OSINT Preset — prepackaged)
key_terms: []
tag_taxonomy:
  domain: ["#osint", "#geopolitics", "#intelligence", "#threat", "#sourcing"]
  context: ["#region", "#actor", "#event", "#timeline"]
deep_dive_topics: []
report_style: "assessment"
custom_directory_mapping: ""
