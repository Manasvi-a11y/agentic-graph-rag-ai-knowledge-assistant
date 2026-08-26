import { useEffect, useRef, useState } from "react";
import api from "../api/api";
import ChatInput from "./ChatInput";
import Message from "./Message";

const SUGGESTIONS = [
  "What is RAG?",
  "Explain relational databases",
  "What is a Turing machine?",
  "What is supervised learning?",
];

function ChatBox({ draftPrompt }) {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const threadRef = useRef(null);

  useEffect(() => {
    if (threadRef.current) {
      threadRef.current.scrollTop = threadRef.current.scrollHeight;
    }
  }, [messages, loading]);

  const sendMessage = async (question) => {
    const priorTurns = messages.filter((m) => m.sender !== "system");
    const userTurn = { sender: "user", text: question };
    const updatedMessages = [...priorTurns, userTurn];

    setMessages((prev) => [...prev, userTurn]);
    setLoading(true);

    try {
      const response = await api.post("/chat", {
        query: question,
        history: updatedMessages,
      });

      const answer =
        response.data.answer ||
        response.data.response ||
        JSON.stringify(response.data);

      setMessages((prev) => [...prev, { sender: "assistant", text: answer }]);
    } catch (error) {
      console.error(error);
      setMessages((prev) => [
        ...prev,
        {
          sender: "system",
          text: "Couldn't reach the assistant. Check your connection and try again.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <div className="thread" ref={threadRef}>
        {messages.length === 0 && (
          <div className="empty">
            <p className="empty__eyebrow">Start here</p>
            <h2 className="empty__title">Ask something you'd find in the index</h2>
            <p className="empty__body">
              Answers are retrieved from the actual subject libraries on the
              left, not guessed — so specific, self-contained questions work
              best.
            </p>
            <div className="empty__suggestions">
              {SUGGESTIONS.map((s) => (
                <button
                  key={s}
                  type="button"
                  className="suggestion"
                  onClick={() => sendMessage(s)}
                >
                  {s}
                </button>
              ))}
            </div>
          </div>
        )}

        {messages.map((msg, index) => (
          <Message key={index} sender={msg.sender} text={msg.text} />
        ))}

        {loading && (
          <div className="thinking">
            <span className="thinking__label">retrieving</span>
            <span className="thinking__path">
              <span className="thinking__node" />
              <span className="thinking__edge" />
              <span className="thinking__node" />
              <span className="thinking__edge" />
              <span className="thinking__node" />
            </span>
          </div>
        )}
      </div>

      <ChatInput
        key={draftPrompt?.id ?? "static"}
        onSend={sendMessage}
        initialText={draftPrompt?.text ?? ""}
        disabled={loading}
      />
    </>
  );
}

export default ChatBox;