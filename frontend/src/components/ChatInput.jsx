import { useState } from "react";

function ChatInput({ onSend, initialText = "", disabled }) {
  const [text, setText] = useState(initialText);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!text.trim() || disabled) return;
    onSend(text.trim());
    setText("");
  };

  return (
    <form onSubmit={handleSubmit} className="composer">
      <div className="composer__field">
        <span className="composer__caret" aria-hidden="true">
          &gt;
        </span>
        <input
          type="text"
          placeholder="Ask anything from the index..."
          value={text}
          onChange={(e) => setText(e.target.value)}
          disabled={disabled}
          autoFocus={Boolean(initialText)}
        />
      </div>
      <button type="submit" disabled={disabled || !text.trim()}>
        Send
      </button>
    </form>
  );
}

export default ChatInput;