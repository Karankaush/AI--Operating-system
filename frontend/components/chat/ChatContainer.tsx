"use client"

import MessageList from "./MessageList"

import ChatInput from "./ChatInput"

import { useChatStore }
from "@/store/chat-store"


export default function ChatContainer() {

  const {
    chats,
    currentChatId
  } = useChatStore()


  const currentChat =
    chats.find(
      (chat) =>
        chat.id === currentChatId
    )


  return (
    <div className="flex flex-1 flex-col bg-zinc-900">

      <div className="flex-1 overflow-y-auto">

        <MessageList
          messages={
            currentChat?.messages || []
          }
        />

      </div>

      <ChatInput />

    </div>
  )
}