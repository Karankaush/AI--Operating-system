"use client"

import { useState } from "react"

import { Send } from "lucide-react"

import { Input } from "@/components/ui/input"

import { Button } from "@/components/ui/button"

import { useChatStore }
from "@/store/chat-store"

import { sendMessage }
from "@/services/chat.service"


export default function ChatInput() {

  const [message, setMessage] =
    useState("")


  const { addMessage } =
    useChatStore()


  const handleSubmit = async () => {

    if (!message.trim()) return


    addMessage({
      role: "user",
      content: message
    })


    const userMessage = message

    setMessage("")


    try {

      const response =
        await sendMessage(userMessage)


      addMessage({
        role: "assistant",
        content: response.response
      })

    } catch (error) {

      console.log(error)
    }
  }


  return (
    <div className="border-t border-zinc-800 bg-zinc-950 p-4">

      <div className="flex items-center gap-3">

        <Input
          value={message}
          onChange={(e) =>
            setMessage(e.target.value)
          }
          placeholder="Ask anything..."
          className="
            border-zinc-700
            bg-zinc-900
            text-white
          "
        />


        <Button
          size="icon"
          onClick={handleSubmit}
          className="
            bg-blue-600
            hover:bg-blue-700
          "
        >
          <Send className="h-4 w-4 text-white" />
        </Button>

      </div>

    </div>
  )
}