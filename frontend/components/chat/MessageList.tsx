import ChatMessage from "./ChatMessage"

import { Message } from "@/types/chat"


type MessageListProps = {
  messages: Message[]
}


export default function MessageList({
  messages
}: MessageListProps) {

  return (
    <div className="flex flex-col gap-4 p-6">

      {messages.map((message, index) => (

        <ChatMessage
          key={index}
          role={message.role}
          content={message.content}
        />

      ))}

    </div>
  )
}