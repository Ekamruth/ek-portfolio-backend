# Experience & Projects — Yeedu (Modak Analytics LLP)

## Company: Modak Analytics LLP
**Employment period: July 2024 – Present**

Modak Analytics LLP is an AI-native data engineering company helping enterprises manage, migrate, and utilise large-scale data ecosystems through cloud-agnostic solutions and AI-powered workflows.

---

## Product: Yeedu — Cloud Data & Spark Performance Platform
**Role: Senior Frontend Engineer**
**Duration: ~13 months | Stack: Vue 3 (Composition API, composables), PrimeVue, JavaScript, Pinia, Vue Router, Server-Sent Events (SSE)**

Yeedu is Modak's SaaS platform for managing and optimising Apache Spark workloads in the cloud. It cuts data processing costs by ~60% and boosts Spark performance without requiring full platform migration or cloud lock-in. It runs entirely within the customer's own cloud account. Customers use it alongside or as an alternative to Databricks and Cloudera. The platform covers cluster management, job orchestration, notebook workflows, workspace management, cloud storage integrations, and enterprise workflow tooling across multiple cloud providers.

Ekamruth was one of the primary frontend contributors on Yeedu, owning major product surfaces end-to-end — from architecture discussions through production delivery.

---

## Feature Ownership & Project Details

### Workspace File Management System
Designed and built the entire workspace and dependency file management system from scratch using Vue 3 and PrimeVue. Users could navigate file trees, upload large files with real-time feedback, rename files in place, and browse folders with infinite scroll. The architecture was built to be reusable and became the shared foundation for notebook, job, and cluster advanced options across the platform — reducing duplication and ensuring UI consistency.

### File Pickers
Built a consistent file-picker experience across every major form in the product — Job, Notebook, Cluster, Spark configs, Yeedu Function, and workspace path selection. Each picker supports infinite scroll, extension filtering, and tree-based navigation, eliminating error-prone manual path entry across the full form surface.

### YeeduAssistantX — AI Assistant
Architected and continuously evolved the AI assistant experience, which became a key differentiator of the Yeedu platform:
- Built the full conversational interface with persistent history, real-time token streaming, and expand/collapse panel
- Rendered tool execution steps inline as the AI worked, giving users operational visibility
- Added chart rendering for AI-generated HTML/JS responses
- Merged two separate AI modes (Code AI and Ops AI) into a single unified AssistantX interface, simplifying the UX significantly
- Built "Diagnose Error with AI" entry points directly inside Cluster and Job dashboards — contributing to a 30–40% decrease in debugging and incident resolution time through contextual error analysis and real-time diagnostic responses
- Shipped LLM model-selection UI, giving operators the ability to switch inference backends
- Integrated slash-command routing from the input bar

### Notebook AI
Built the Notebook AI interface inside Yeedu notebooks — live response simulation, syntax highlighting, and rich rendering of code output, enabling AI-assisted data exploration directly within the notebook environment.

### Catalog Explorer
Built the Catalog Explorer — a full data asset browser allowing users to explore schemas and tables across Unity Catalog, Hive, and CDP Hive providers in one unified interface. Added context-menu actions and quick workspace path copy to streamline developer workflows.

### Unity Catalog Integration
Implemented the Unity Catalog UI end-to-end — covering create and edit flows, metastore management, secrets configuration, access tab UX, and error recovery. Handled the full product surface from initial setup through ongoing editing and operational management.

### Mounts Feature
Built the complete storage mount lifecycle management feature, enabling users to create, configure, and manage cloud storage mounts with role-based access controls. Deeply integrated with the cluster creation workflow so mount selection was part of the natural setup flow.

### Secrets Validation and Management
Redesigned the secrets management system, reducing frontend complexity by 66% while improving validation, security handling, and usability. Built validate-on-demand flows with inline error surfacing so users caught configuration issues immediately rather than at job execution time. Fixed multiple gaps in "Create Secret" flows across different provider configurations that were blocking users from completing setup.

### PrimeVue Component Migration
Led the migration to PrimeVue across the product — standardizing the component library, improving UI consistency, and enabling better performance through modern data table rendering including skeleton loading states, infinite scroll, and filterable dashboards. Created a shared table loader component adopted across multiple dashboards, reducing UI inconsistency and development effort for new screens. Cut UI development time on new features by ~40% and eliminated thousands of lines of duplicated code.

### Notebook Reliability
Resolved critical notebook rendering issues including cell output display failures, code being cleared on advanced options update, and "page not responding" crashes on large log files. These were high-impact reliability issues directly affecting developer productivity. Added a Turbo enable/disable toggle accessible directly from within the notebook.

### Production Quality & Release Management
- Owned 70+ feature stories and resolved 55+ production bugs over 13 months with a near-zero regression rate
- Consistently shipped across Jobs, Billing, Import/Export, and Clusters while maintaining release stability across 14 active branches
- Proactively added test IDs across major features to enable automated E2E testing, going beyond feature delivery to support the QA pipeline
- Maintained and delivered work across multiple concurrent release branches simultaneously, managing upstream syncs and version-specific fixes without regressions
