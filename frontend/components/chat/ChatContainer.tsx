import MessageList from "./MessageList"
import ChatInput from "./ChatInput"


export default function ChatContainer() {
  return (
    <div className="flex flex-1 flex-col bg-zinc-900">

      <div className="flex-1 overflow-y-auto">

        <MessageList />

      </div>

      <ChatInput />

    </div>
  )
}