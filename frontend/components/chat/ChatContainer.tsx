import MessageList from  "./MessageList"

export default function ChatContainer() {
  return (
    <div className="flex-1 overflow-y-auto bg-zinc-900">
      <MessageList />
    </div>
  )
}