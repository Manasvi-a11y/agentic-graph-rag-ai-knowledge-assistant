import { useState } from "react";
import api from "../api/api";
import ChatInput from "./ChatInput";
import Message from "./Message";

function ChatBox() {
  const [messages, setMessages] = useState([]);

  const sendMessage = async (question) => {
    const updatedMessages = [
      ...messages,
      { sender: "user", text: question }
    ];

    setMessages(updatedMessages);

    try {
      const response = await api.post("/chat", {
        query: question,
        history: updatedMessages,
      });

      const answer =
        response.data.answer ||
        response.data.response ||
        JSON.stringify(response.data);

      setMessages((prev) => [
        ...prev,
        { sender: "assistant", text: answer },
      ]);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          sender: "assistant",
          text: "Error connecting to backend.",
        },
      ]);
    }
  };

  return (
    <div className="chat-container">
      <div className="messages">
        {messages.map((msg, index) => (
          <Message
            key={index}
            sender={msg.sender}
            text={msg.text}
          />
        ))}
      </div>

      <ChatInput onSend={sendMessage} />
    </div>
  );
}

export default ChatBox;