# Install the Drapalski AI Skills Library

This is an **AI-agent add-on**, not a stand-alone website or chatbot. These instructions are written for Windows users but the commands are cross-platform.

## What you need

1. A computer with internet access.
2. [Node.js LTS](https://nodejs.org/) (the installer includes npm and `npx`).
3. An AI application that supports [Agent Skills](https://agentskills.io/), such as a compatible release of Claude Code or Cursor.

## A. Install in Windows Command Prompt

Open **Command Prompt** (`cmd`) and verify Node.js:

```bat
node --version
npx --version
```

Both commands should print version numbers. If not, install Node.js LTS and reopen Command Prompt.

List the Skills offered by this GitHub repository (optional check):

```bat
npx skills add drapalski/drapalski-management-accounting-skills --list
```

Install and follow the interactive prompts:

```bat
npx skills add drapalski/drapalski-management-accounting-skills -g
```

The `-g` flag makes the installed Skills available to the selected agent across your local projects. If you prefer to install only for one project, omit `-g` and run the command in that project's directory.

## B. Start learning

Open the AI agent you selected. Try:

> Use study-coach to diagnose my understanding of contribution margins. Ask me one question at a time and do not give the full solution until I request it.

Or:

> Use activity-based-costing. Explain cost pools and cost drivers, then give me a new fictional two-product example to solve.

The AI assistant may need to restart or open a new conversation to discover newly installed Skills. Agent behaviour and skill activation vary across applications.

## C. Updating and troubleshooting

```bat
npx skills list -g
npx skills update
```

If the `list -g` flag is unsupported by your installed CLI version, use `npx skills list` and consult `npx skills --help`.

**`npx` not recognized:** install Node.js LTS, close and reopen your terminal.  
**No compatible agent detected:** install a supported agent first and then rerun the command.  
**Skill not found in agent:** inspect the install prompts, restart the agent, and ask it explicitly to use the Skill name.  
**The agent gives a dubious answer:** cross-check equations, dimensions, assumptions, and the answer-check section of the practice case.  
**Install offers unexpected permissions:** inspect the package and CLI before accepting; never give credentials to unknown code.

## What this does not do

- It does not create a ChatGPT Custom GPT or public web app.
- It does not upload personal accounting data anywhere by itself; however the chosen AI agent may process anything you send it under its own terms.
- It does not guarantee every Agent Skills-compatible product behaves identically.

For the official installer options, see [skills.sh CLI documentation](https://www.skills.sh/docs/cli).
