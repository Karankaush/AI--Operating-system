type SidebarItemProps = {
  title: string
}


export default function SidebarItem({
  title
}: SidebarItemProps) {

  return (
    <button
      className="
        w-full
        rounded-lg
        px-3
        py-2
        text-left
        text-sm
        text-zinc-300
        hover:bg-zinc-800
      "
    >
      {title}
    </button>
  )
}