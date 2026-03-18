---
name: cuiz-ai
description: Context about Cuiz AI — Nelson's AI quiz & flashcard generator from documents (Next.js + FastAPI + Firebase). Project overview, architecture, links, and key concepts.
disable-model-invocation: true
---

# Cuiz AI — Project Context

This skill provides context about Cuiz AI so you can have informed conversations about it. **You do not code on this project** — delegate all coding tasks to the `coder` subagent.

## What Is Cuiz AI

An AI-powered platform that generates interactive quizzes and flashcards from uploaded documents (PDF, DOC, PPT, TXT). Users upload study material, the system processes it through LLMs, and produces quizzes with difficulty levels and flashcards with spaced repetition (SM-2 algorithm). Supports multiple languages.

**Domain:** `cuiz-ai.com`
**Monetization:** Stripe subscription with usage limits.

## Links

- **GitHub:** https://github.com/nelsongallardo/cuiz-ai
- **Local code:** `~/projects/cuiz-ai/`
- **Production:** https://cuiz-ai.com

## Tech Stack

| Layer | Tech |
|-------|------|
| Frontend | Next.js 15, React 19, TypeScript, Tailwind, shadcn/ui (Radix) |
| Backend | Python, FastAPI, Pydantic |
| Database | Cloud Firestore |
| Auth | Firebase Authentication |
| Storage | AWS S3 (document uploads via presigned URLs) |
| LLMs | OpenRouter (Gemini Flash primary, OpenAI/Claude/Llama/Grok fallbacks) |
| Payments | Stripe |
| Analytics | PostHog (frontend + backend middleware) |
| Error Monitoring | Sentry (frontend), GCP Error Reporting (backend) |
| Email | Email Octopus (contacts, welcome emails, re-engagement) |
| Deployment | Vercel (frontend), GCP (backend) |

## Project Structure

```
~/projects/cuiz-ai/
├── quiz-ai-generator-frontend/   # Next.js 15 app
├── quiz-ai-generator-api/        # FastAPI backend
├── webhook/                      # Webhook handlers
├── CLAUDE.md                     # Root project instructions
├── PRODUCT_STRATEGY.md           # Product strategy doc
└── TODO.md                       # Current tasks
```

## Architecture Overview

### Core Data Flow
1. User uploads document → S3 presigned URL
2. Backend parses document (PDF/DOC/PPT/TXT) → text chunking (8k token limit)
3. LLM generates quiz questions via OpenRouter
4. Quiz stored in Firestore under user
5. User can generate flashcards from quiz (LLM transformation)
6. Spaced repetition (SM-2) tracks flashcard mastery
7. Export to PDF/DOCX available

### Backend (quiz-ai-generator-api/)
- **Document processing pipeline:** reader factory → chunking → LLM generation
- **LLM routing:** all providers through OpenRouter using OpenAI SDK, primary model `google/gemini-3-flash-preview:nitro`
- **Flashcard service:** LLM-based quiz-to-flashcard transformation + SM-2 spaced repetition
- **Rate limiting:** slowapi (IP + token based)
- **Scheduled jobs:** Cloud Scheduler triggers inactive user sync → Email Octopus tagging (7/14/30 day buckets)
- **Analytics middleware:** PostHog request tracking at middleware level

### Frontend (quiz-ai-generator-frontend/)
- **Next.js 15 App Router** with React 19
- **Key pages:** landing, upload, quiz taking, flashcard practice, dashboard, library, pricing, blog
- **Blog system:** markdown files in `content/blog/` with gray-matter + react-markdown
- **SEO:** comprehensive — sitemaps, robots.txt, JSON-LD schemas, OG/Twitter cards, search engine verification
- **Cookie consent:** PostHog gated behind consent
- **Sample demos:** `/sample-quiz` and `/sample-flashcards` for anonymous users

### Key Features
1. **Document upload & processing** — multi-format with intelligent chunking
2. **Quiz generation** — AI-powered with difficulty levels (low/med/high) and language support
3. **Flashcard generation** — LLM transforms quiz into flashcards
4. **Spaced repetition** — SM-2 algorithm for review scheduling
5. **Quiz taking** — interactive interface with scoring and review
6. **Export** — PDF/DOCX
7. **Quiz library** — history, retake, manage
8. **Subscription** — Stripe billing with usage limits
9. **Blog** — markdown-based with SEO
10. **Re-engagement** — Email Octopus tagging for inactive users via scheduled jobs

## When Nelson Talks About Cuiz AI

Common topics you might hear about:
- Quiz generation from documents and LLM quality
- Flashcard system and spaced repetition
- OpenRouter model selection and fallbacks
- Document processing and token chunking
- Stripe subscriptions and pricing
- PostHog analytics and conversion tracking
- SEO and blog content
- Email re-engagement campaigns
- The upload flow and S3 presigned URLs
- Sample/demo quizzes for marketing

## Coding Tasks → Delegate

When Nelson asks to build, fix, or modify anything in Cuiz AI:

```
sessions_spawn task:"<describe the task> — project is at ~/projects/cuiz-ai/" agentId:"coder"
```

Do NOT attempt to code yourself. The coder subagent has Claude Code CLI which will read the project's own CLAUDE.md files for detailed coding instructions.
