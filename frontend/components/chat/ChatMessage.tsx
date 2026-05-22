
type ChatMessageProps = {
    role : "user" | "assistant"
    content : string
}

export default function ChatMessage({role,content}: ChatMessageProps) {
    const isUser = role == "user"

    return(
         <div
      className={`flex w-full ${
        isUser ? "justify-end": "justify-start"}`}>
            
        <div
        className={`max-w-[70%] rounded-2xl px-4 py-3 text-sm text-white ${
          isUser
            ? "bg-blue-600"
            : "bg-zinc-800"
        }`}>
        {content}

      </div>
    </div>

    )
}