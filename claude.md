# AI Guidance and Coding Standards - Flashcard App

## Context and Role
You are an AI coding assistant helping to build a Flashcard study application. The primary goal is to build a highly structured, simple, and correct system that focuses on clear boundaries, interface safety, and maintainability.

## Core Constraints & AI Instructions
To protect system integrity and maintain code quality, you must adhere to the following rules at all times:

1. **Simplicity Over Cleverness:** Write readable, predictable code. Avoid overly complex abstractions. Simple code is better than clever code.
2. **Correctness:** Ensure your generated code prevents invalid states and explicitly enforces business rules.
3. **Interface Safety:** 
   - Guard against misuse. 
   - Validate all inputs (types, schemas, required fields) at the API or component boundaries.
4. **Change Resilience:** Structure new features so they do not cause widespread impact to existing functional code.
5. **Observability:** Ensure failures are visible and diagnosable. Return meaningful error messages and log appropriately.
6. **No Unprompted Refactoring:** Do not rewrite existing working components unless explicitly asked.

## Tech Stack Rules

### Backend (Python/Flask + SQLite)
- **Structure:** Use Flask Blueprints to enforce clear route boundaries.
- **Data Access:** Use SQLAlchemy ORM. Abstract database interactions cleanly.
- **Validation:** Enforce basic type checks and validate required fields on every incoming request. Reject invalid data with `400 Bad Request`.
- **Responses:** Always return proper HTTP status codes (200, 201, 400, 404, 500) and structured JSON error messages.

### Frontend (React)
- **Structure:** Functional components with hooks. Keep components focused on a single responsibility.
- **Data Layer:** Centralize API calls in `/src/api/index.js`.
- **State & UX:** Always show loading states for async operations. Provide basic, clear error handling to the user on failures.

### Testing & Verification
- Prioritize testability. Write automated tests (e.g., using `pytest` for backend API routes) proving behavior remains correct.

---

## AI Usage Documentation (For Evaluators)

*This section documents how AI was utilized during the development of this project.*

* **Guidance and Constraints:** This `claude.md` file was used as the primary instruction set to constrain AI behavior, enforce coding standards, and protect the system architecture.
* **Development Flow:** AI was utilized to scaffold boilerplate code, refine Flask API routing logic, and explore edge cases for testing.
* **Review & Verification:** All AI-generated code was critically reviewed by the developer, tested against edge cases (ex: missing fields, invalid IDs), and refactored to ensure it prioritized readable simplicity over complexity. The final architectural decisions and code ownership belong entirely to the developer.
