# Product Testing Framework

## What This Question Tests
Tests your ability to identify which aspects of a feature to test and what techniques to use — with a goal-first, hypothesis-driven approach.

## Evaluation Criteria
- Do you start with the product goal before identifying what to test?
- Do you identify *what* to test and *why*?
- Do you understand common testing techniques like A/B testing?
- Is your answer structured and coherent?

---

## The Framework

### Step 1: Describe the Feature
What does the feature do? What is the user-facing experience?

### Step 2: State the Goal of the Feature
What is the feature trying to achieve?
- Example: "People You May Know" goal = help users grow their professional network by connecting with relevant people

### Step 3: Identify Components
Break the feature into its distinct components or sub-experiences:
- What does each component do?
- Which components are most likely to affect the feature's goal?

### Step 4: Hypothesize Design Alternatives
For each component worth testing, form a hypothesis about a design alternative:
- What might work better?
- What is the expected impact on the goal metric?

> Format: "We believe that [design change] will [improve metric] because [reason]."

### Step 5: Define How to Test Each Hypothesis

**A/B Testing**: Split users randomly between the current version (control) and the new version (variant). Measure the impact on the goal metric.
- Requires: sufficient traffic, clear success metric, clean experiment design (one variable at a time)

**User Interviews / Usability Testing**: Qualitative testing with a small sample of users. Best for understanding *why* users behave a certain way.

**Multivariate Testing**: Test multiple variables simultaneously. Better for optimization when you have high traffic.

**Canary Release**: Roll out to a small % of users first to detect issues before full launch.

### Step 6: Summarize and Recommend
- Which 1–2 components are worth testing first?
- Why? (highest impact on goal, or most uncertain assumptions?)
- What is the success metric for each test?
- What are the guardrail metrics (what you'd watch to prevent unintended harm)?

---

## Example
**"How would you test LinkedIn's 'People You May Know' feature?"**

- **Goal**: Increase high-quality connections
- **Components**: Suggestion algorithm, card design, placement in feed, call-to-action copy
- **Hypothesis 1**: Showing thumbnails instead of text links will increase connection rate (warmer, more personal)
- **Hypothesis 2**: Showing mutual connections prominently will increase acceptance rate
- **Test**: A/B test on connection rate and quality (message exchange rate as a proxy for meaningful connections)
- **Guardrail**: Don't sacrifice user trust by surfacing unexpected/irrelevant suggestions

---

## Common Question Examples
- "How would you test LinkedIn's 'People You May Know' feature?"
- "How would you test a new checkout flow?"
- "How do you know when a feature is ready to launch?"
- "Walk me through how you'd A/B test [feature]."

## Coaching Tips
- Goal-first is the biggest differentiator — testing without a goal produces noise, not insight
- Be specific about the metric you'd use to declare a winner — vague answers like "see if it performs better" aren't sufficient
- Mention guardrail metrics — shows you're thinking about unintended consequences
- A/B testing has constraints (traffic, duration, novelty effect) — acknowledging them shows maturity
