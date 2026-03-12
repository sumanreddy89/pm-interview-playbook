# PM Interview Playbook

A comprehensive, open-source library of product management interview frameworks — covering every major question type you'll encounter in PM interviews at top tech companies.

Each framework explains **what the question tests**, **how interviewers evaluate your answer**, and provides a **step-by-step structure** with coaching tips and example questions.

> **New to this repo?** The frameworks are readable markdown files — just click any file in the `frameworks/` folder and GitHub will render them as clean, formatted text. No installation needed to use them as reference material. If you want the interactive coaching experience, see [How to Use This Repo](#how-to-use-this-repo) below.

---

## What's Included

### The Claude Skill: `pm-interview-coach`

The headline feature of this repo is a **Claude skill** that turns these static frameworks into an interactive interview coaching experience.

Once installed, you can say things like:
- *"Practice a metrics question with me"*
- *"Run me through a mock PM interview"*
- *"Give me feedback on my answer to a product improvement question"*
- *"How do I structure an estimation question?"*

Claude will follow the frameworks, ask follow-up questions like a real interviewer, and give you specific, actionable feedback based on the exact evaluation criteria that real interviewers use.

→ **[How to use this repo](#how-to-use-this-repo)**

---

### The Framework Library

23 frameworks across 6 categories:

#### Strategy
| Framework | What It Covers |
|-----------|---------------|
| [Growth Strategy](frameworks/growth.md) | Analyzing competitive landscape and market drivers to recommend growth initiatives |
| [New Market Entry](frameworks/new-market-entry.md) | Evaluating whether a company should enter a new market |
| [Pricing Strategy](frameworks/pricing.md) | Choosing the right pricing model based on market, competition, and goals |
| [Marketing Plan](frameworks/marketing-plan.md) | Goal-first marketing analysis and activity planning |
| [Monetization](frameworks/monetization.md) | Identifying and prioritizing revenue models for a product or service |
| [Goal Setting](frameworks/goal-setting.md) | Defining business objectives and product goals top-down |

#### Execution
| Framework | What It Covers |
|-----------|---------------|
| [Prioritization](frameworks/prioritization.md) | Using RICE to compare two competing product options |
| [Problem Diagnostic](frameworks/problem-diagnostic.md) | Root-cause analysis when a metric drops |
| [Metrics](frameworks/metrics.md) | Defining North Star, goal metrics, and health metrics |
| [Product Development Trade-offs](frameworks/product-development.md) | Comparing two product development options across multiple dimensions |
| [Cost-Benefit Analysis](frameworks/cost-benefit.md) | Strategic and financial evaluation of investment decisions |

#### Product Design
| Framework | What It Covers |
|-----------|---------------|
| [Design a New Product](frameworks/design-new-product.md) | From ideation to launchable concept: segment, pain, solution |
| [Product Improvement](frameworks/product-improve.md) | Business-goal-driven product improvement analysis |
| [Product Critique](frameworks/product-critique.md) | Evaluating design using first principles |
| [Favorite Product](frameworks/fav-product.md) | Demonstrating product intuition and design depth |
| [Product Launch](frameworks/product-launch.md) | Pre/during/post launch planning |
| [Product Testing](frameworks/product-testing.md) | Hypothesis-driven A/B testing and feature validation |

#### Analytical
| Framework | What It Covers |
|-----------|---------------|
| [Estimation](frameworks/estimation.md) | Two approaches to back-of-the-envelope estimation |
| [Metrics](frameworks/metrics.md) | *(also in Execution)* |
| [Cost-Benefit Analysis](frameworks/cost-benefit.md) | *(also in Execution)* |

#### Behavioral & Soft Skills
| Framework | What It Covers |
|-----------|---------------|
| [Behavioral / Situational](frameworks/behavioral.md) | CACRL story structure for experience-based questions |
| [Fit / Recruiter Screen](frameworks/fit.md) | Tell me about yourself, why here, why hire you |
| [Brainstorming](frameworks/brainstorming.md) | SCAMPER technique for divergent thinking questions |

#### Technical
| Framework | What It Covers |
|-----------|---------------|
| [System Design](frameworks/system-design.md) | PM-focused systems design: users, requirements, scaling |
| [Technology Knowledge](frameworks/technology.md) | DNS, HTTP, TCP/IP and other technical concepts PMs should know |

---

## How to Use This Repo

There are three ways to use this, depending on what you want:

---

### Option 1: Just read the frameworks (no installation needed)

You don't need to install anything. Every framework is a plain markdown file that GitHub renders as clean, formatted text.

1. Browse the [`frameworks/`](frameworks/) folder above
2. Click any file — it opens in your browser as a formatted page
3. Read, study, and prep

That's it. No accounts, no apps, no downloads. This works on any device.

---

### Option 2: Interactive coaching with Cowork (Claude Desktop)

This gives you an AI coach that will run mock interviews, give feedback on your answers, and teach you frameworks interactively.

1. Download `pm-interview-coach.skill` from the [Releases](../../releases) page
2. Open [Claude Desktop](https://claude.ai/download) and go to **Cowork mode**
3. Drag the `.skill` file into the chat (or use the skill installer in settings)
4. Say something like *"Practice a metrics question with me"* or *"Run me through a mock PM interview"*

Claude will follow the frameworks, ask follow-up questions like a real interviewer, and give you specific feedback based on the exact criteria that interviewers use.

---

### Option 3: Use with Claude Code (for developers)

If you use [Claude Code](https://claude.ai/claude-code) in your terminal:

1. Clone this repo
2. Copy the skill folder to your Claude skills directory:
   ```bash
   cp -r pm-interview-coach/ ~/.claude/skills/
   ```
3. In any Claude Code session, say *"Let's practice PM interview questions"* and the skill will be available

---

### Option 4: Fork and customize

Fork this repo and adapt the frameworks to your own interview style, add your own examples, or build on top of the skill. See [Contributing](#contributing) for ideas.

---

## How the Frameworks Are Structured

The `frameworks/` folder contains 23 markdown (`.md`) files — one per question type. Markdown is plain text with simple formatting. On GitHub, every file renders as a nicely formatted page you can read in your browser, no app or installation required.

Each file follows the same structure:
- **What the question tests** — the underlying competency being evaluated
- **Evaluation criteria** — the specific signals interviewers look for
- **Step-by-step framework** — how to structure your answer
- **Example questions** — common variants you might encounter
- **Coaching tips** — the most important things to get right

You can use them purely as reading material, or pair them with the Claude skill for active practice.

---

## Contributing

This library is open source and contributions are welcome! Ways to contribute:
- Add example answers demonstrating frameworks in action
- Add new question types not currently covered
- Improve existing frameworks based on your interview experiences
- Add company-specific tips (Amazon LP, Google PM interviews, etc.)

Please open a PR or file an issue.

---

## About the Author

Built by **Suman Reddy** — a product manager who went through the PM interview grind and wanted to make structured prep more accessible to everyone.

If you're looking for PM mentoring, interview coaching, or just want to connect, visit **[sumanreddy.me](https://www.sumanreddy.me)**.

---

*If this helped you land a PM role, consider starring the repo and sharing it with others preparing for interviews.*
