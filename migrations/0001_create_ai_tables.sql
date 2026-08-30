-- Cloudflare D1 Migration 0001: Ask Karnata AI Knowledge & Multi-Tier Caching System

-- 1. Knowledge Base Documents for RAG & Retrieval
CREATE TABLE IF NOT EXISTS ai_documents (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  url TEXT,
  category TEXT NOT NULL,
  language TEXT DEFAULT 'kn',
  source_type TEXT DEFAULT 'karnata', -- 'karnata' | 'official_eci' | 'official_gov'
  source_url TEXT,
  keywords TEXT,
  published_at TEXT,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 2. Curated & Verified Fast FAQs (SIR, Schemes, Administration)
CREATE TABLE IF NOT EXISTS ai_faq (
  id TEXT PRIMARY KEY,
  question TEXT NOT NULL,
  normalized_question TEXT NOT NULL,
  answer TEXT NOT NULL,
  category TEXT NOT NULL, -- 'SIR' | 'VOTER' | 'SCHEME' | 'OFFICER' | 'AGRICULTURE' | 'GENERAL'
  language TEXT DEFAULT 'kn',
  source_url TEXT,
  keywords TEXT,
  action_label TEXT,
  action_url TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 3. Multi-Tier Cache with TTL & Hit Counter
CREATE TABLE IF NOT EXISTS ai_cache (
  id TEXT PRIMARY KEY,
  normalized_question TEXT UNIQUE NOT NULL,
  answer TEXT NOT NULL,
  language TEXT DEFAULT 'kn',
  sources_json TEXT,
  cards_json TEXT,
  hit_count INTEGER DEFAULT 1,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  expires_at INTEGER NOT NULL
);

-- 4. Anonymized AI Observability & Performance Logs (NO PII)
CREATE TABLE IF NOT EXISTS ai_queries (
  id TEXT PRIMARY KEY,
  normalized_question TEXT NOT NULL,
  language TEXT DEFAULT 'kn',
  intent TEXT,
  cache_hit BOOLEAN DEFAULT 0,
  faq_hit BOOLEAN DEFAULT 0,
  ai_used BOOLEAN DEFAULT 0,
  latency_ms INTEGER,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Indexing for sub-millisecond lookups
CREATE INDEX IF NOT EXISTS idx_ai_faq_normalized ON ai_faq(normalized_question);
CREATE INDEX IF NOT EXISTS idx_ai_faq_category ON ai_faq(category);
CREATE INDEX IF NOT EXISTS idx_ai_cache_normalized ON ai_cache(normalized_question);
CREATE INDEX IF NOT EXISTS idx_ai_docs_category ON ai_documents(category);
CREATE INDEX IF NOT EXISTS idx_ai_docs_keywords ON ai_documents(keywords);
