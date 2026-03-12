# Cost-Benefit Analysis Framework

## What This Question Tests
Tests how you make business decisions when there are costs and benefits to weigh — using both strategic parameters and financial analysis.

## Evaluation Criteria
- Do you clearly state your evaluation approach upfront?
- Are you exhaustive in identifying all relevant inputs?
- Can you apply basic financial reasoning (NPV)?
- Articulate, structured, and succinct?

---

## The Framework

### Step 1: Clarify
Ask questions to understand context:
- Is this a standalone product or a platform tool?
- What is the timeline for the decision?
- Are there resource or budget constraints?

### Step 2: Frame the Problem
Restate the problem clearly:
- What are the two options?
- What is the decision criterion? (e.g., which is better for the business long-term?)

### Step 3: Identify Strategic Inputs
Before calculating anything, analyze the strategic parameters that affect the decision:

| Input | What to Assess |
|-------|---------------|
| **Market maturity** | Emerging/growing markets justify investment; mature/declining markets don't |
| **Reusability** | Can this feature/tool be reused across products? Platform = higher ROI |
| **Time to build** | Will it be ready before the market matures? |
| **Speed lift** | How much faster does this make future development? (set a target multiple) |

All four prerequisites must be met to proceed to financial analysis:
- Market is emerging or growing ✓
- Feature/tool is highly reusable ✓
- Ready before market matures ✓
- Meets target speed-of-development improvement ✓

### Step 4: Financial Analysis (NPV)
If strategic prerequisites are met, calculate the Net Present Value:

```
NPV = (Σ Savings / (1 + r)^t) - Cost of building

Where:
  Savings (S) = engineering labor cost saved per period
  r = discount rate (quarterly or annual)
  t = number of periods during product lifetime
  Cost (C) = upfront investment to build
```

If NPV > 0, the investment is justified. Otherwise, it's not.

### Step 5: Recommendation
Provide a clear recommendation with conditions:
> "I recommend building the tool *if*: (1) it's for a platform, (2) the market is emerging/growing, and (3) the NPV is positive. Otherwise, no."

---

## Example
**"How would you prioritize a new product feature vs. an internal tool that builds it faster?"**

Key insight: If the tool is for a platform (not just one product), reusability across multiple products makes it more likely to justify the cost. A single-use tool rarely passes the NPV test unless the feature is extremely expensive to build manually.

---

## Common Question Examples
- "How would you prioritize building an internal tool vs. shipping a product feature?"
- "Is it worth investing in [infrastructure/platform] vs. building directly?"
- "We can improve developer productivity by 3x with a 6-month investment. Is it worth it?"

## Coaching Tips
- Strategic prerequisites matter as much as the financial model — investing in a tool for a declining market is a bad idea even if the NPV looks positive
- NPV is the right tool here because it accounts for the time value of money — mention it even if you don't calculate it precisely
- Involve engineering, finance, and product in the decision — mention cross-functional input as part of your process
- A flowchart or decision tree is a great way to summarize your framework visually (mention that you'd draw one)
