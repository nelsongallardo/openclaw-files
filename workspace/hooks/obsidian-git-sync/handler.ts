import { execFile } from "node:child_process";
import { promisify } from "node:util";

const execFileAsync = promisify(execFile);

const VAULT = "/Users/openclaw/Documents/obsidian";
const REMOTE = "origin";
const BRANCH = "main";
const COMMIT_MESSAGE = "auto: update from OpenClaw";

async function runGit(args: string[]) {
  return execFileAsync("git", args, { cwd: VAULT, timeout: 30000 });
}

async function syncVault() {
  try {
    const status = await runGit(["status", "--porcelain"]);
    if (!status.stdout.trim()) return;

    await runGit(["add", "-A"]);

    const cached = await runGit(["diff", "--cached", "--quiet"]).then(
      () => false,
      (error: any) => {
        if (typeof error?.code === "number") {
          return error.code === 1;
        }
        return false;
      },
    );

    if (!cached) return;

    await runGit(["commit", "-m", COMMIT_MESSAGE]);
    await runGit(["push", REMOTE, BRANCH]);
    console.log("[obsidian-git-sync] synced vault changes");
  } catch (error) {
    console.error("[obsidian-git-sync] sync failed", error);
  }
}

const handler = async (event: any) => {
  if (event?.type !== "message" || event?.action !== "sent") return;
  void syncVault();
};

export default handler;
