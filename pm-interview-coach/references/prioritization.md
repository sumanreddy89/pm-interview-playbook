# Prioritization Framework

## What This Question Tests
Tests how you handle trade-offs between two competing product issues, initiatives, or options — with a structured, data-informed approach.

## Evaluation Criteria
- Do you ask clarifying questions?
- Do you have a structured approach for comparing options?
- Do you consider multiple data points?
- Clear and succinct communication?

---

## The Framework (4 Steps)

### Step 1: Clarify
Ask questions to understand the scope:
- What are the constraints? (timeline, resources, budget)
- Are these the only two options, or could we do both?
- What's the company's current most important goal?

### Step 2: Context (Business Framing)
Set the business context before comparing options:
- **Company**: What does the company do?
- **Product**: What is the product's goal?
- **Revenue model**: How does the company make money?
- **Lifecycle**: Where is the product (new, growing, mature)?
- **Competitors**: How is the company doing vs. competitors?
- **Business goal**: Based on the above, what is the most important thing to achieve right now?

This gives you a *criterion* to use when comparing the two options.

### Step 3: Compare Using RICE
Evaluate each option across the RICE framework:

| Dimension | Description |
|-----------|-------------|
| **Reach** | How many users are affected? |
| **Impact** | How much does this move the business goal? (scale: 0.25, 0.5, 1, 2, 3) |
| **Confidence** | How confident are you in your estimates? (%) |
| **Effort** | How many person-months to build? |

**RICE Score** = (Reach × Impact × Confidence) / Effort

The higher the RICE score, the higher the priority.

### Step 4: Recommend
Synthesize your comparison into a clear recommendation:
- Which issue/option should be prioritized, and why?
- What are the risks of deprioritizing the other?
- Is there a sequencing that lets you do both over time?

---

## Example
**"As an Airbnb PM, how do you prioritize fixing sign-in problems vs. complaints about dirty places?"**

- **Context**: Airbnb's goal is marketplace growth and trust; reviews/trust are a core differentiator
- **Sign-in issue**: Reach (all users trying to book), Impact (blocking conversions directly), Confidence (measurable), Effort (medium)
- **Dirty places**: Reach (fraction of completed bookings), Impact (affects retention and reviews, high long-term), Confidence (medium), Effort (requires host-side changes, high)
- **Recommendation**: Sign-in issue scores higher because it blocks the conversion funnel for all users — a leaky funnel prevents you from even getting users to the point where they'd encounter the dirty places issue. Fix the funnel first.

---

## Common Question Examples
- "Should we fix [bug A] or build [feature B]?"
- "We have 5 items on the roadmap and can only ship 2 this quarter. How do you decide?"
- "How do you prioritize between a major enterprise customer request and the product roadmap?"
- "As Airbnb PM, prioritize: sign-in problems vs. dirty place complaints."

## Coaching Tips
- The business goal is your North Star for comparison — without it, RICE is just arithmetic
- Be explicit about assumptions in your RICE scores; the reasoning matters more than the numbers
- Often the "right" answer is less important than showing *how* you'd decide
- Mention stakeholder input — real prioritization decisions involve engineering, design, and data
