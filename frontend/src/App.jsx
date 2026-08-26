import { useState } from "react";
import Sidebar from "./components/Sidebar";
import ChatBox from "./components/ChatBox";

function App() {
  const [draftPrompt, setDraftPrompt] = useState(null);

  const handlePick = (label) => {
    setDraftPrompt({ text: `Explain ${label}`, id: Date.now() });
  };

  return (
    <div className="shell">
      <Sidebar onPick={handlePick} />
      <main className="main">
        <header className="header">
          <h1 className="header__title">Agentic Graph RAG</h1>
          <p className="header__subtitle">
            Knowledge assistant · grounded across 17 subject libraries
          </p>
        </header>
        <ChatBox draftPrompt={draftPrompt} />
      </main>
    </div>
  );
}

export default App;