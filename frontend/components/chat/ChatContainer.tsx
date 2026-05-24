"use client"

import MessageList from "./MessageList"

import ChatInput from "./ChatInput"

import { useChat } from "@/hooks/useChat"


export default function ChatContainer() {

  const {
    messages,
    handleSendMessage
  } = useChat()


  return (
    <div className="flex flex-1 flex-col bg-zinc-900">

      <div className="flex-1 overflow-y-auto">

        <MessageList
          messages={messages}
        />

      </div>

      <ChatInput
        onSendMessage={handleSendMessage}
      />

    </div>
  )
}