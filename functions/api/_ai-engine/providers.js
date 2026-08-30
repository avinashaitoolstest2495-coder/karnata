/**
 * Ask Karnata AI — Multi-Model Provider Abstraction Layer
 * Supports Cloudflare Workers AI, future Ollama local server, and Gemini.
 */

export class BaseAIProvider {
  async generateAnswer(options) {
    throw new Error('generateAnswer() must be implemented by subclass');
  }
}

/**
 * Cloudflare Workers AI Provider (Default ₹0 Edge Provider)
 */
export class CloudflareWorkersAIProvider extends BaseAIProvider {
  constructor(env) {
    super();
    this.env = env;
  }

  async generateAnswer({ prompt, systemPrompt, maxTokens = 800, temperature = 0.2 }) {
    if (!this.env || !this.env.AI) {
      throw new Error('Cloudflare Workers AI binding [env.AI] is not available.');
    }

    const primaryModel = this.env.AI_MODEL || '@cf/meta/llama-3.1-8b-instruct';
    const fallbackModel = '@cf/meta/llama-3.2-3b-instruct';

    try {
      const resp = await this.env.AI.run(primaryModel, {
        messages: [
          { role: 'system', content: systemPrompt },
          { role: 'user', content: prompt }
        ],
        max_tokens: maxTokens,
        temperature: temperature
      });

      if (resp && (resp.response || resp.text)) {
        return {
          answer: (resp.response || resp.text).trim(),
          model: primaryModel,
          providerName: 'Cloudflare Workers AI (Llama 3.1 8B)'
        };
      }
    } catch (primaryErr) {
      console.warn(`[Primary Model ${primaryModel} Error, trying fallback ${fallbackModel}]:`, primaryErr);

      const fallbackResp = await this.env.AI.run(fallbackModel, {
        messages: [
          { role: 'system', content: systemPrompt },
          { role: 'user', content: prompt }
        ],
        max_tokens: maxTokens,
        temperature: temperature
      });

      if (fallbackResp && (fallbackResp.response || fallbackResp.text)) {
        return {
          answer: (fallbackResp.response || fallbackResp.text).trim(),
          model: fallbackModel,
          providerName: 'Cloudflare Workers AI (Llama 3.2 3B Fallback)'
        };
      }
    }

    throw new Error('Workers AI did not return a valid response.');
  }
}

/**
 * Self-Hosted Ollama Provider (Future Expansion)
 */
export class OllamaProvider extends BaseAIProvider {
  constructor(endpoint = 'http://localhost:11434', model = 'llama3.1:8b') {
    super();
    this.endpoint = endpoint;
    this.model = model;
  }

  async generateAnswer({ prompt, systemPrompt }) {
    const res = await fetch(`${this.endpoint}/api/generate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: this.model,
        prompt: `${systemPrompt}\n\nUser: ${prompt}\nAssistant:`,
        stream: false
      })
    });
    const data = await res.json();
    return {
      answer: data.response,
      model: this.model,
      providerName: 'Self-Hosted Ollama Engine'
    };
  }
}

/**
 * Provider Factory
 */
export function getAIProvider(env) {
  // Default to Cloudflare Workers AI
  return new CloudflareWorkersAIProvider(env);
}
