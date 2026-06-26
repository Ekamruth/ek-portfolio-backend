# Experience & Projects — ForgeAI (Modak Analytics LLP)

## Company: Modak Analytics LLP
**Employment period: July 2024 – Present**

Modak Analytics LLP is an AI-native data engineering company helping enterprises manage, migrate, and utilise large-scale data ecosystems through cloud-agnostic solutions and AI-powered workflows.

---

## Product: ForgeAI — AI-First Data Engineering Platform
**Role: Senior Frontend Engineer**
**Duration: ~6 months | Stack: Vue 3 (Composition API, composables), JavaScript, Pinia, Vue Router, Server-Sent Events (SSE)**

ForgeAI is Modak's end-to-end AI-first data engineering platform. It automates profiling, mapping, coding, testing, and debugging of data pipelines — enabling data engineering in minutes instead of weeks. The platform integrates deeply with GitHub, Jira, Databricks, Yeedu, cloud storage, and enterprise data sources. A core concept is the Workstream — a persistent AI project workspace where conversations retain full contextual awareness of connected enterprise systems, repositories, tickets, and infrastructure.

Ekamruth was the **sole frontend owner of the ForgeAI chat interfaces** — the most critical and flagship feature of the platform. Other ForgeAI modules (pipeline automation, context graph, policy fabric, etc.) were handled by other engineers. His scope was exclusively the chat interfaces.

---

## Feature Ownership & Project Details

### Multi-Conversation Streaming Engine
Architected a streaming engine that broke a hard single-session bottleneck — taking concurrent live AI conversations from 1 → unlimited and lifting stream survival across app navigation from 0% → 100%, so users never lose an in-flight response again.

### Chat Architecture Refactor — Userstories & Workstreams
Built both core conversational systems — Userstories and Workstreams — from scratch. Collapsed 2 monolithic chat surfaces into 1 unified streaming core and a shared composable library — cutting duplicated real-time logic paths in half and turning every future chat feature into a single-touch change instead of two. Reduced code duplication by 40–70% through reusable composable systems and modular rendering pipelines.

### Design-First Streaming Rewrite
De-risked the most complex feature on the roadmap before writing a line of code by authoring a versioned design spec with a full state machine, data-flow diagrams, and 17 pre-defined test scenarios — shipping the streaming rewrite with zero rollback and an incremental, feature-flagged migration.

### Real-Time Job Monitoring (Yeedu Job Tracking in Chat)
Engineered a real-time job-monitoring system with conversation-scoped visibility and background polling that survives route changes, delivering 100% of terminal-status outcomes (success/error/timeout) as live notifications — eliminating the need for users to babysit long-running data jobs. Built Yeedu Job Tracking inside the chat UI, polling job status and visualising state transitions in real time directly within the conversation.

### SSE-Based Streaming & State Synchronisation
Implemented real-time SSE-based streaming and workflow state synchronisation so users could see AI work happening live. Managed complex state for multi-chat workstreams, persistent conversation history, and async operational workflows.

### Conversation History Pagination
Replaced all-at-once history rendering with incremental pagination and scroll-up lazy loading, slashing initial chat-load cost on heavy conversations.

### Streaming Reliability Hardening
Added heartbeat keep-alives and timeout recovery for long-running AI operations, resolving the top user-blocking defects — tool-call render corruption and full-UI freezes on stream completion.

### User-Facing Chat Features
Shipped 10+ user-facing capabilities end-to-end — including Git-style conversation branching, a slash-command palette, read-only access controls, chat sharing, and custom instruction layers — owning each from design through production.

### Performance Optimisation
Optimised application performance via route-level code splitting and lazy loading, reducing bundle size by 70% and improving load times by 60%.

### Internal AI Agent & Engineering Guidelines
Built and deployed an internal "Chat UI Specialist" AI agent plus standardised engineering guidelines, scaling consistent frontend delivery beyond a single contributor.
