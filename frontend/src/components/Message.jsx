function Message({ sender, text }) {
  return (
    <div className={`message ${sender}`}>
      <strong>{sender === "user" ? "You" : "Assistant"}:</strong>
      <p style={{ whiteSpace: "pre-wrap" }}>{text}</p>
    </div>
  );
}

export default Message;