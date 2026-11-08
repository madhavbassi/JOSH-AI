
import { useEffect, useRef, useState } from 'react';
import { ArrowRight, ArrowUp, FileText, Home, Layers3, UserRound } from 'lucide-react';
import CelestialSphere from './components/CelestialSphere.jsx';
import VoiceGreeting from './components/voicegreeting.jsx';
import './styles.css';

const questions = [
  "What is Madhav's CGPA?",
  "Tell me about Madhav's projects.",
  'What technologies has Madhav used?',
  'What is Madhav studying?',
  'What experience and leadership roles does Madhav have?',
];

const navigation = [
  { label: 'Home', Icon: Home, action: 'home' },
  { label: 'About Madhav', Icon: UserRound, prompt: "Tell me about Madhav's background." },
  { label: 'Projects & Builds', Icon: Layers3, prompt: "Tell me about Madhav's projects." },
  { label: 'Resume (PDF)', Icon: FileText, action: 'resume' },
];

const apiUrl = import.meta.env.VITE_CHAT_API_URL?.trim();
const requestField = import.meta.env.VITE_CHAT_REQUEST_FIELD?.trim() || 'question';
const responseField = import.meta.env.VITE_CHAT_RESPONSE_FIELD?.trim() || 'answer';
const resumeUrl = import.meta.env.VITE_RESUME_URL?.trim();

function valueAtPath(value, path) {
  return path.split('.').filter(Boolean).reduce((current, key) => current?.[key], value);
}

function getAnswer(payload) {
  if (typeof payload === 'string') return payload;
  const selected = valueAtPath(payload, responseField);
  if (typeof selected === 'string') return selected;
  if (typeof payload?.response === 'string') return payload.response;
  if (typeof payload?.message === 'string') return payload.message;
  if (typeof payload?.content === 'string') return payload.content;
  return '';
}

function App() {
  const [messages, setMessages] = useState([]);
  const [draft, setDraft] = useState('');
  const [loading, setLoading] = useState(false);
  const [notice, setNotice] = useState('');
  const chatEnd = useRef(null);
  const inputRef = useRef(null);
  const isChat = messages.length > 0;

  useEffect(() => {
    chatEnd.current?.scrollIntoView({ behavior: 'smooth', block: 'end' });
  }, [messages, loading]);

  async function submitQuestion(rawQuestion) {
    const question = rawQuestion.trim();
    if (!question || loading) return;
    setNotice('');
    setDraft('');
    setMessages((current) => [...current, { role: 'user', text: question }]);

    if (!apiUrl) {
      setMessages((current) => [...current, {
        role: 'assistant',
        error: true,
        text: 'JOSH’s chat service is not connected yet. Set VITE_CHAT_API_URL to your existing FastAPI chat endpoint, then try again.',
      }]);
      return;
    }

    setLoading(true);
    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify({ [requestField]: question }),
      });

      const raw = await response.text();
      let payload;
      try {
        payload = raw ? JSON.parse(raw) : {};
      } catch {
        payload = raw;
      }

      if (!response.ok) {
        const detail = typeof payload === 'object' ? payload?.detail || payload?.error : '';
        throw new Error(detail || `The chat service returned HTTP ${response.status}.`);
      }

      const answer = getAnswer(payload);
      if (!answer) {
        throw new Error(`The endpoint returned no text in “${responseField}”. Check VITE_CHAT_RESPONSE_FIELD or your API response.`);
      }

      setMessages((current) => [...current, { role: 'assistant', text: answer }]);
    } catch (error) {
      setMessages((current) => [...current, {
        role: 'assistant',
        error: true,
        text: error instanceof TypeError
          ? 'JOSH could not reach the configured chat service. Check the endpoint and its CORS settings, then try again.'
          : error.message || 'The chat request failed. Please try again.',
      }]);
    } finally {
      setLoading(false);
    }
  }

  function handleSubmit(event) {
    event.preventDefault();
    submitQuestion(draft);
  }

  function handleNav(item) {
    if (item.action === 'home') {
      setMessages([]);
      setNotice('');
      setDraft('');
      return;
    }

    if (item.action === 'resume') {
      if (resumeUrl) window.open(resumeUrl, '_blank', 'noopener,noreferrer');
      else setNotice('Resume PDF is not connected yet. Set VITE_RESUME_URL to the resume endpoint.');
      return;
    }

    submitQuestion(item.prompt);
  }

  return (
    <div className="app-shell">

      {/* JOSH welcome voice */}
      <VoiceGreeting />

      <aside className="sidebar" aria-label="Main navigation">
        <a className="brand" href="#home" onClick={(e) => { e.preventDefault(); handleNav(navigation[0]); }}>
          <span className="brand-mark" aria-hidden="true"><span /></span>
          <span className="brand-copy"><strong>JOSH</strong><small>Personal AI Assistant</small></span>
        </a>

        <div className="sidebar-rule" />

        <nav className="nav-list">
          {navigation.map(({ label, Icon, ...item }) => (
            <button key={label} className={`nav-item ${label === 'Home' && !isChat ? 'active' : ''}`} onClick={() => handleNav(item)}>
              <Icon size={17} strokeWidth={1.65} aria-hidden="true" />
              <span>{label}</span>
              {label === 'Resume (PDF)' && <ArrowRight className="nav-arrow" size={13} aria-hidden="true" />}
            </button>
          ))}
        </nav>

        <div className="sidebar-bottom">
          <span className="live-dot" />
          <span>Available for inquiries</span>
        </div>
      </aside>

      <main className="main-panel" id="home">
        <header className="topbar">
          <div className="mobile-brand">
            <span className="brand-mark" aria-hidden="true"><span /></span>
            <strong>JOSH</strong>
          </div>
          <p className="online-status"><span className="live-dot" /> JOSH Online <i>·</i> Ready for inquiries</p>
          <p className="representing">Representing Madhav Bassi</p>
        </header>

        {!isChat ? (
          <section className="home-stage" aria-label="JOSH homepage">
            <div className="ambient ambient-one" />
            <div className="ambient ambient-two" />

            <div className="hero-content">
              <div className="orb-entry"><CelestialSphere /></div>
              <h1>Hi, I'm <span>JOSH.</span></h1>
              <p className="subtitle">I am Madhav's personal assistant.</p>

              <div className="question-list" aria-label="Suggested questions">
                {questions.map((question) => (
                  <button className="suggestion" key={question} onClick={() => submitQuestion(question)}>
                    <span>{question}</span>
                    <ArrowRight size={14} strokeWidth={1.6} aria-hidden="true" />
                  </button>
                ))}
              </div>
            </div>

            <Composer draft={draft} setDraft={setDraft} onSubmit={handleSubmit} inputRef={inputRef} loading={loading} />

            {notice && <div className="inline-notice" role="status">{notice}</div>}
          </section>
        ) : (
          <section className="conversation-stage" aria-label="Conversation with JOSH">
            <div className="messages" aria-live="polite">
              {messages.map((message, index) => (
                <div className={`message-row ${message.role} ${message.error ? 'error' : ''}`} key={`${index}-${message.role}`}>
                  {message.role === 'assistant' && <span className="assistant-glyph" aria-hidden="true"><span /></span>}
                  <div className="message-bubble">{message.text}</div>
                </div>
              ))}

              {loading && (
                <div className="message-row assistant">
                  <span className="assistant-glyph" aria-hidden="true"><span /></span>
                  <div className="message-bubble typing"><i /><i /><i /></div>
                </div>
              )}

              <div ref={chatEnd} />
            </div>

            <Composer draft={draft} setDraft={setDraft} onSubmit={handleSubmit} inputRef={inputRef} loading={loading} conversation />

            {notice && <div className="inline-notice conversation-notice" role="status">{notice}</div>}
          </section>
        )}
      </main>
    </div>
  );
}

function Composer({ draft, setDraft, onSubmit, inputRef, loading, conversation = false }) {
  return (
    <form className={`composer-wrap ${conversation ? 'conversation-composer' : ''}`} onSubmit={onSubmit}>
      <div className="composer-halo" aria-hidden="true" />

      <div className="composer">
        <div className="composer-input-row">
          <input
            ref={inputRef}
            value={draft}
            onChange={(event) => setDraft(event.target.value)}
            placeholder="Ask JOSH about Madhav..."
            aria-label="Ask JOSH about Madhav"
            autoComplete="off"
            disabled={loading}
          />
        </div>

        <div className="composer-controls">
          <div className="composer-identity" aria-label="JOSH personal AI assistant">
            <span className="composer-orb" aria-hidden="true"><span /></span>
            <span>JOSH</span>
            <span className="composer-separator" aria-hidden="true" />
            <span className="composer-context">PERSONAL AI</span>
          </div>

          <button className="send-button" type="submit" disabled={!draft.trim() || loading} aria-label="Send question">
            <ArrowUp size={17} strokeWidth={1.8} />
          </button>
        </div>
      </div>
    </form>
  );
}

export default App;
