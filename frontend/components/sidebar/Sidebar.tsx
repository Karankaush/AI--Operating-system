import PdfUpload from "../upload/PdfUpload"


export default function Sidebar() {

  return (
    <div className="w-[280px] border-r border-zinc-800 bg-zinc-950">

      <div className="p-4">

        <h1 className="text-xl font-bold text-white">
          AI OS
        </h1>

      </div>

      <PdfUpload />

    </div>
  )
}