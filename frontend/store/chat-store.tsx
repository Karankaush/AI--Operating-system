"use client"

import {
  createContext,
  useContext,
  useState
} from "react"

import { Message } from "@/types/chat"


type Chat = {
  id: number
  title: string
  messages: Message[]
}


type ChatContextType = {
  chats: Chat[]

  currentChatId: number

  setCurrentChatId: (
    id: number
  ) => void

  addMessage: (
    message: Message
  ) => void

  createNewChat: () => void
}


const ChatContext =
  createContext<ChatContextType | null>(
    null
  )


export function ChatProvider({
  children
}: {
  children: React.ReactNode
}) {

  const [chats, setChats] = useState<Chat[]>([
    {
      id: 1,
      title: "New Chat",
      messages: []
    }
  ])


  const [currentChatId, setCurrentChatId] =
    useState(1)


  const addMessage = (
    message: Message
  ) => {

    setChats((prevChats) =>
      prevChats.map((chat) => {

        if (chat.id === currentChatId) {

          return {
            ...chat,
            messages: [
              ...chat.messages,
              message
            ]
          }
        }

        return chat
      })
    )
  }


  const createNewChat = () => {

  const newChat = {
    id: Date.now(),
    title: "New Chat",
    messages: []
  }


  setChats((prev) => [
    ...prev,
    newChat
  ])


  setCurrentChatId(newChat.id)
}


  return (
    <ChatContext.Provider
      value={{
    chats,
    currentChatId,
    setCurrentChatId,
    addMessage,
    createNewChat
  }}
    >
      {children}
    </ChatContext.Provider>
  )
}


export function useChatStore() {

  const context =
    useContext(ChatContext)

  if (!context) {

    throw new Error(
      "useChatStore must be used inside ChatProvider"
    )
  }

  return context
}