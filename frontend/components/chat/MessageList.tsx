import ChatMessage from "./ChatMessage"


const messages = [
  {
    role: "assistant",
    content: "Hello, I am your AI OS."
  },
  {
    role: "user",
    content: "Tell me about LangGraph."
  },
  {
    role: "assistant",
    content: "LangGraph is a knowledge graph that connects all your data, files, and tools in one place. It allows you to easily access and manage your information, and provides powerful search and organization capabilities."
  },
  {
    role: "user",
    content: "Tell me about LangGraph."
  }
]


export default function MessageList() {
  return (
    <div className="flex flex-col gap-4 p-6">

      {messages.map((message, index) => (
        <ChatMessage
          key={index}
          role={message.role as "user" | "assistant"}
          content={message.content}
        />
      ))}

    </div>
  )
}