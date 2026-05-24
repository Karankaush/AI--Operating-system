"use client"

import { useState } from "react"

import { Send } from "lucide-react"

import { Input } from "@/components/ui/input"

import { Button } from "@/components/ui/button"


type ChatInputProps = {
  onSendMessage: (message: string) => void
}


export default function ChatInput({
  onSendMessage
}: ChatInputProps) {

  const [message, setMessage] =
    useState("")


  const handleSubmit = () => {

    if (!message.trim()) return

    onSendMessage(message)

    setMessage("")
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
          className="border-zinc-700 bg-zinc-900 text-white"
        />

        <Button
          size="icon"
          onClick={handleSubmit}
          className="bg-blue-600 hover:bg-blue-700"
        >
          <Send className="h-4 w-4 text-white" />
        </Button>

      </div>

    </div>
  )
}