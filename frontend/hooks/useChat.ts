"use client"

import { useState } from "react"

import { Message } from "@/types/chat"

import { sendMessage } from "@/services/chat.service"


export function useChat() {

  const [messages, setMessages] =
    useState<Message[]>([])


  const handleSendMessage = async (
    message: string
  ) => {

    if (!message.trim()) return


    const userMessage: Message = {
      role: "user",
      content: message
    }


    setMessages((prev) => [
      ...prev,
      userMessage
    ])


    try {

      const response = await sendMessage(
        message
      )


      const aiMessage: Message = {
        role: "assistant",
        content: response.response
      }


      setMessages((prev) => [
        ...prev,
        aiMessage
      ])

    } catch (error) {

      console.log(error)
    }
  }


  return {
    messages,
    handleSendMessage
  }
}