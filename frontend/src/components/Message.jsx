import ReactMarkdown from "react-markdown";

const ROLE_LABEL = {
  user: "You",
  assistant: "Assistant",
  system: "System",
};

function Message({ sender, text }) {
  return (
    <div className={`msg msg--${sender}`}>
      <div className="msg__role">
        <span className="msg__dot" aria-hidden="true" />
        {ROLE_LABEL[sender] || sender}
      </div>
      <div className="msg__card">
        {sender === "assistant" ? (
          <ReactMarkdown>{text}</ReactMarkdown>
        ) : (
          <p>{text}</p>
        )}
      </div>
    </div>
  );
}

export default Message;