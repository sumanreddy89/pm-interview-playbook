# Technology Knowledge Framework

## What This Question Tests
Tests whether you have enough technical understanding to work credibly with engineers, debug technical discussions, and understand how products work under the hood.

## Evaluation Criteria
- Can you explain technical concepts accurately and clearly?
- Can you connect technical concepts to product decisions?
- Are you comfortable discussing complexity without being intimidated by it?

---

## Key Question: "What happens when you enter a URL in a browser?"

This is a canonical PM technical question. Here's a complete walkthrough:

### High-Level Flow
1. Browser checks its **cache** (and OS cache) for the IP address matching the URL
2. If not cached, browser sends a **DNS query** to the DNS resolver (via ISP)
3. DNS resolver performs a **recursive lookup**: root DNS → TLD server (.COM) → authoritative name server → returns IP
4. Browser establishes a **TCP connection** with the web server at that IP
5. Browser sends an **HTTP GET/POST request** over TCP (with headers: User-Agent, Accept, cookies, etc.)
6. Web server receives request → passes to **application handler** → queries database → assembles HTML response
7. Server returns response with **status code**, headers (compression, caching, cookies), and HTML body
8. Browser **renders the HTML**, then fires additional GET requests for CSS, JavaScript, images (caches them)

### Key Technical Concepts for PMs

**DNS (Domain Name System)**: Translates human-readable URLs to IP addresses. Think of it as the phone book of the internet.

**TCP/IP**: TCP handles reliable connection establishment (3-way handshake: SYN, SYN-ACK, ACK). IP handles routing packets across the network.

**HTTP/HTTPS**: Application-level protocol for client-server communication. HTTPS adds TLS encryption over HTTP.

**CDN (Content Delivery Network)**: Distributes static assets (images, CSS, JS) to servers geographically close to users — reduces latency.

**Caching**: Storing responses at multiple levels (browser, CDN, server) to avoid redundant computation.

**REST vs. GraphQL**: REST uses resource-based endpoints; GraphQL lets clients specify exactly what data they need.

**Client vs. Server rendering**: SSR (server-side rendering) sends fully rendered HTML; CSR (client-side rendering) sends a skeleton and renders via JavaScript.

---

## Other Common Technical Questions

**"What are the technical details of a product you worked on?"**
- Describe the key components, data flows, and notable technical decisions/trade-offs

**"What happens when you swipe a credit card?"**
- Card → POS terminal → payment processor (Visa/MC network) → issuing bank (authorization) → back to merchant → settlement batch at end of day

**"Tell me about the most complex product you've worked on."**
- Focus on: the technical challenges, trade-offs you helped navigate, how you worked with engineering to make decisions

---

## Coaching Tips
- You don't need to know every detail — but you should be able to have a fluent conversation about the tech
- When asked about your own product, be ready to go one level deeper on any component
- Interviewers often follow up with "why?" — prepare to explain the reasoning behind technical choices, not just what they are
- Connecting technical details to user experience is where PMs differentiate from engineers ("we chose a CDN because users in Southeast Asia were experiencing 4s load times, which was killing engagement")
