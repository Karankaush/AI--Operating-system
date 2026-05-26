"use client"

import PdfUpload from "../upload/PdfUpload"

import SidebarItem from "./SidebarItem"

import { Plus } from "lucide-react"

import { useChatStore }
from "@/store/chat-store"


export default function Sidebar() {

  const {
  chats,
  currentChatId,
  setCurrentChatId,
  createNewChat
} = useChatStore()


  return (
    <div className="w-[280px] border-r border-zinc-800 bg-zinc-950">

      <div className="p-4">

        <h1 className="text-xl font-bold text-white">
          AI OS
        </h1>


        <button
        onClick={createNewChat}
          className="
            mt-4
            flex
            w-full
            items-center
            gap-2
            rounded-lg
            bg-zinc-800
            px-3
            py-2
            text-sm
            text-white
            hover:bg-zinc-700
          "
        >
          <Plus className="h-4 w-4" />

          New Chat

        </button>

      </div>


      <PdfUpload />


      <div className="p-4">

        <h2 className="mb-3 text-sm font-semibold text-zinc-400">

          Chats

        </h2>


        <div className="flex flex-col gap-2">

          {chats.map((chat) => (

            <div
              key={chat.id}
              onClick={() =>
                setCurrentChatId(chat.id)
              }
            >

              <SidebarItem
                title={chat.title}
              />

            </div>

          ))}

        </div>

      </div>

    </div>
  )
}