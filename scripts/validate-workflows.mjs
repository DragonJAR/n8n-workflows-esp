import { readFileSync } from "node:fs";

function validateWorkflow(path) {
  const failures = [];
  let workflow;

  try {
    workflow = JSON.parse(readFileSync(path, "utf8"));
  } catch (error) {
    return [`${path}: invalid JSON (${error.message})`];
  }

  const nodes = Array.isArray(workflow.nodes) ? workflow.nodes : [];
  if (nodes.length === 0) failures.push(`${path}: nodes must not be empty`);

  const names = new Set();
  const ids = new Set();
  for (const node of nodes) {
    if (node === null || typeof node !== "object" || Array.isArray(node)) {
      failures.push(`${path}: every node must be an object`);
      continue;
    }
    if (typeof node.name !== "string" || node.name.trim() === "") {
      failures.push(`${path}: every node must have a name`);
    } else if (names.has(node.name)) {
      failures.push(`${path}: duplicate node name "${node.name}"`);
    } else {
      names.add(node.name);
    }

    if (typeof node.id === "string" && node.id !== "") {
      if (ids.has(node.id)) {
        failures.push(`${path}: duplicate node id "${node.id}"`);
      }
      ids.add(node.id);
    }
  }

  for (const [source, outputs] of Object.entries(workflow.connections ?? {})) {
    if (!names.has(source)) {
      failures.push(`${path}: missing connection source "${source}"`);
    }
    for (const routes of Object.values(outputs ?? {})) {
      if (!Array.isArray(routes)) continue;
      for (const route of routes) {
        if (!Array.isArray(route)) continue;
        for (const connection of route) {
          if (
            typeof connection?.node === "string" &&
            !names.has(connection.node)
          ) {
            failures.push(
              `${path}: missing connection target "${connection.node}"`,
            );
          }
        }
      }
    }
  }

  return failures;
}

const paths = process.argv.slice(2);
if (paths.length === 0) {
  process.stderr.write(
    "Usage: node scripts/validate-workflows.mjs workflows/example.json\n",
  );
  process.exitCode = 2;
} else {
  const failures = paths.flatMap(validateWorkflow);
  if (failures.length > 0) {
    for (const failure of failures) process.stderr.write(`ERROR ${failure}\n`);
    process.exitCode = 1;
  } else {
    process.stdout.write(`Validated ${paths.length} workflow files.\n`);
  }
}
