# System Design Framework (PM-Focused)

## What This Question Tests
Tests whether you understand enough about distributed systems to discuss technical trade-offs with engineers — with a product-oriented lens (users, use cases, requirements first).

## Evaluation Criteria
- **Technical knowledge**: Can you discuss APIs, databases, client/server, front/backend?
- **Functional requirements**: Can you translate product choices into system requirements?
- **Bottlenecks/scaling**: Can you identify where systems break under load and how to fix it?

---

## The Framework

### Step 1: Users
Describe who the users are and why they want to use the product.
- Primary and secondary users
- Key behavioral characteristics (read-heavy vs. write-heavy usage?)

### Step 2: Use Cases
Explain what users should be able to accomplish with the product.
- List the 3–5 core use cases
- Prioritize: which use case is most critical?

### Step 3: Functional Requirements
List the technical requirements to support the core use cases:
- Input/output data types
- Required system behaviors (e.g., real-time vs. eventual consistency, latency requirements)
- Authentication/authorization needs

### Step 4: Design Considerations
Ask clarifying questions about constraints:
- How long should data be stored?
- What's the max size of a message/post/artifact?
- What's the expected scale (users, requests per second)?
- Geographic distribution requirements?

### Step 5: Assumptions
State your top system assumptions:
- "I'll assume this is read-heavy (10:1 reads to writes)"
- "I'll prioritize availability over strong consistency (eventual consistency is acceptable)"

### Step 6: Data Structures
Describe how data is organized and stored:
- What are the main entities? (User, Post, Message, etc.)
- How are they related?
- What storage type fits? (SQL for structured data, NoSQL for flexible/high-scale, blob storage for media)

### Step 7: High-Level Design
Sketch the main components and explain how they connect:
- Client(s) → API Gateway → Application Layer → Database(s)
- For each component: what does it do? What protocol? (REST, WebSocket, gRPC?)
- Walk through the flow for your primary use case

### Step 8: Scale the Design
Identify bottlenecks and explain how to address them:

| Bottleneck | Solution |
|-----------|----------|
| Database reads at scale | Read replicas, caching (Redis/Memcached) |
| Database writes at scale | Sharding, write-ahead log, message queue (Kafka) |
| Single point of failure | Load balancer + horizontal scaling |
| High-latency media delivery | CDN for static assets |
| Compute-heavy operations | Async processing with queues |

---

## Common Question Examples
- "Design a URL shortener."
- "Design Twitter's feed."
- "Design a notification system."
- "Design a ride-sharing matching system."

## Coaching Tips
- As a PM, you don't need to be as deep as an engineer — but you should show you can hold a real technical conversation
- The user + use case section differentiates you: engineers often skip it, PMs should lead with it
- Always acknowledge trade-offs — "we chose availability over consistency because users care more about seeing *something* than seeing the *exact* latest state"
- Drawing a diagram (even roughly described verbally) makes your answer much clearer
